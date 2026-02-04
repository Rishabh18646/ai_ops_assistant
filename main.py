from fastapi import FastAPI
from agents.planner import planner_agent
from agents.exectutor import executor_agent
from agents.verifier import verifier_agent
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(".")))

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Ops Assistant Running"}

@app.post("/run")
def run_task(task: str):
    plan = planner_agent(task)
    execution = executor_agent(plan)
    verification = verifier_agent(execution)

    return {
        "plan": plan,
        "execution": execution,
        "verification": verification
    }
