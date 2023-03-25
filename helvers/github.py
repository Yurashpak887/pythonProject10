import json
import requests

def get_github_repositories(query, page, per_page):
    response = requests.get("https://api.github.com/search/repositories?q=" + query + "&page=" + page + "&per_page=" + per_page)
    return response.content


def json_parser(body):
    data = json.loads(body)
    repo = []
    for i in data["items"]:
        new_repo = {
            "name": i["name"],
            "full_name": i["full_name"],
            "private": i["private"],
            "description": i["description"]
        }
        repo.append(new_repo)
    return repo