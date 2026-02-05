import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def github_tool(query):
    return search_github_repo(query)

def search_github_repo(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    r = requests.get(url, headers=headers)
    
    if r.status_code != 200:
        return {"error": "GitHub API failed"}

    data = r.json()
    if "items" not in data:
        return {"error": "Invalid GitHub response"}

    repo = data["items"][0]
    return {
        "name": repo["name"],
        "stars": repo["stargazers_count"],
        "description": repo["description"],
    }