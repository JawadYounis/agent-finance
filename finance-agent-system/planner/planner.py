from planner.graph import FinanceGraph
from memory.blackboard import GlobalBlackboard

class Planner:
    def __init__(self):
        self.blackboard = GlobalBlackboard()
        self.graph = FinanceGraph()

    def process_task(self, task_text):
        result = self.graph.run(task_text)
        
        return {
            "task": task_text,
            "plan": result["plan"],
            "agent": "LangGraph Orchestrator",
            "result": result["final_answer"],
            "intermediate_results": result["results"]
        }
