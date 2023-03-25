import requests
def get_github_repositories(query):
    response = requests.get("https://api.github.com/search/repositories?q="+query)
    print(response)
