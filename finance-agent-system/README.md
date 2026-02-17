# Finance Multi-Agent System (Phase 1)

A state-of-the-art multi-agent financial orchestration system built with **LangGraph**, **Groq LLM**, and **FastAPI**.

## Features
- **Dynamic Intent Translation**: Human queries are decomposed into actionable sub-tasks.
- **Specialized Expert Agents**: Financial Analyst, Risk Specialist, and Investment Advisor.
- **Collaborative Memory**: Shared "Global Blackboard" for real-time data persistence.
- **Rapid Inference**: Powered by Groq's LPU architecture.

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   Create a `.env` file in `finance-agent-system/` and add your Groq API key:
   ```text
   GROQ_API_KEY=your_key_here
   ```

3. **Run the server**:
   ```bash
   cd finance-agent-system
   $env:PYTHONPATH = "."
   python api/server.py
   ```

## Documentation
For detailed system architecture and API specifications, please refer to:
[**DOCUMENTATION.md**](file:///d:/antigravity/DrFarkhund/Agentic/finance-agent-system/DOCUMENTATION.md)

## Testing the API
```bash
curl -X POST "http://localhost:8001/run-task" \
     -H "Content-Type: application/json" \
     -d '{"task": "Evaluate the financial health of a company with high debt but high growth"}'
```
