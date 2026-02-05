from llm.llm_client import call_llm
import json

def verifier_agent(execution_results):
    prompt = """
    You are a Verifier Agent.
    Check if execution results are complete, correct,
    and formatted cleanly.

    Return JSON strictly:
    {
        "verified": true/false,
        "final_answer": {}
    }
    """

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": json.dumps(execution_results)}
    ]

    result = call_llm(messages)

    try:
        return json.loads(result)
    except:
        return {"verified": False, "error": "Verifier failed", "raw": result}
