from llm.llm_client import call_llm
import json

def planner_agent(user_input):
    prompt = f"""
    Convert this task into a JSON plan with steps and required tools.
    Tools available: github_tool, weather_tool.

    User task: "{user_input}"

    Respond strictly in JSON:
    {{
        "steps": [
            {{"action": "", "tool": "", "input": ""}}
        ]
    }}
    """

    plan = call_llm(prompt)
    return json.loads(plan)