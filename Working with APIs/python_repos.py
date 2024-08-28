import requests

# Make an API call and store the response.
url = "https://api.github.com/search/repositories" # here we are using the headers parameter to pass the Accept header to the API
url += "?q=language:python+sort:stars+stars:>10000"
# The Accept header tells the API that we want the data in JSON format
headers = {"Accept": "application/vnd.github.v3+json"}
# r is the response object that contains the API response
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
# here we are checking if the value of the key 'incomplete_results' is False
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("Selected information about each repository:")

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")



