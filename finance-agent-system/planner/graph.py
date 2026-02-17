import os
import json
from typing import TypedDict, List, Annotated, Dict, Any
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from memory.blackboard import GlobalBlackboard
from agents.financial_analyst import FinancialAnalyst
from agents.risk_compliance import RiskComplianceAgent
from agents.investment_advisor import InvestmentAdvisor

class AgentState(TypedDict):
    query: str
    plan: List[Dict[str, str]]
    results: List[Dict[str, Any]]
    final_answer: str

class FinanceGraph:
    def __init__(self):
        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        self.blackboard = GlobalBlackboard()
        self.agents = {
            "analyst": FinancialAnalyst(),
            "risk": RiskComplianceAgent(),
            "investment": InvestmentAdvisor()
        }
        self.workflow = self._create_workflow()

    def _create_workflow(self):
        graph = StateGraph(AgentState)

        #  nodes
        graph.add_node("planner", self.plan_tasks)
        graph.add_node("executor", self.execute_tasks)
        graph.add_node("summarizer", self.summarize_results)

        #  edges
        graph.set_entry_point("planner")
        graph.add_edge("planner", "executor")
        graph.add_edge("executor", "summarizer")
        graph.add_edge("summarizer", END)

        return graph.compile()

    def plan_tasks(self, state: AgentState):
        """Translate intent into sub-tasks for specific agents."""
        prompt = f"""
        You are a financial orchestrator. Break down the user's query into specific sub-tasks for these experts:
        1. analyst (Financial Analyst): Deals with financial health, statements, growth, and debt.
        2. risk (Risk & Compliance): Deals with market risks, compliance, and debt risks.
        3. investment (Investment Advisor): Deals with investment strategies and stock suggestions.

        Query: {state['query']}

        Return a JSON list of tasks. Example:
        [
            {{"agent": "analyst", "task": "Evaluate financial health of X"}},
            {{"agent": "risk", "task": "Assess market risks for X"}}
        ]
        Return ONLY valid JSON.
        """
        try:
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:-3].strip()
            plan = json.loads(content)
        except Exception:
            # Plan fallback
            plan = [{"agent": "analyst", "task": state['query']}]

        self.blackboard.append_log(f"Graph Planner created plan: {json.dumps(plan)}")
        return {"plan": plan, "results": []}

    def execute_tasks(self, state: AgentState):
        """Run the agents based on the plan."""
        results = []
        for step in state["plan"]:
            agent_name = step["agent"]
            task = step["task"]
            
            if agent_name in self.agents:
                agent = self.agents[agent_name]
                self.blackboard.append_log(f"Graph executing: {agent_name} for task: {task}")
                agent_result = agent.run(task)
                results.append({
                    "agent": agent_name,
                    "task": task,
                    "result": agent_result
                })
        
        return {"results": results}

    def summarize_results(self, state: AgentState):
        """Synthesize all agent findings into a final response."""
        context = json.dumps(state["results"], indent=2)
        
        prompt = f"""
        You are a Senior Investment Officer. Summarize the findings from our specialist agents into a professional final response.
        
        User Query: {state['query']}
        
        Findings:
        {context}
        
        Provide a cohesive, professional response.
        """
        
        try:
            response = self.llm.invoke([SystemMessage(content=prompt), HumanMessage(content="Synthesize the report.")])
            self.blackboard.write("last_result", response.content)
            return {"final_answer": response.content}
        except Exception as e:
            return {"final_answer": f"Error synthesizing results: {str(e)}"}

    def run(self, query: str):
        initial_state = {
            "query": query,
            "plan": [],
            "results": [],
            "final_answer": ""
        }
        return self.workflow.invoke(initial_state)
