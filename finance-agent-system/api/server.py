from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from planner.planner import Planner
from memory.blackboard import GlobalBlackboard
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Finance Multi-Agent System API")
planner = Planner()
blackboard = GlobalBlackboard()

class TaskRequest(BaseModel):
    task: str

@app.post("/run-task")
async def run_task(request: TaskRequest):
    try:
        result = planner.process_task(request.task)
        return {
            "task": result["task"],
            "agent": result["agent"],
            "plan": result.get("plan"),
            "result": result["result"],
            "intermediate_results": result.get("intermediate_results"),
            "blackboard": blackboard.get_all()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
