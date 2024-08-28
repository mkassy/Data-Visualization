import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
title = {'text': 'Most-Starred Python Projects on GitHub', 'x': 0.5, 'xanchor': 'center'}
url = "https://api.github.com/search/repositories" # here we are using the headers parameter to pass the Accept header to the API
url += "?q=language:python+sort:stars+stars:>10000"
# The Accept header tells the API that we want the data in JSON format
headers = {"Accept": "application/vnd.github.v3+json"}
# r is the response object that contains the API response
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': title,
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
