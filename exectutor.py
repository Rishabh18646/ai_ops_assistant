from tools.github_tool import github_tool
from tools.weather_tool import weather_tool

def executor_agent(plan):
    results = []

    for step in plan.get("steps", []):
        tool = step["tool"]
        value = step["input"]

        if tool == "github_tool":
            results.append({"step": step, "result": github_tool(value)})

        elif tool == "weather_tool":
            results.append({"step": step, "result": weather_tool(value)})

        else:
            results.append({"step": step, "result": {"error": "Unknown tool"}})

    return results
