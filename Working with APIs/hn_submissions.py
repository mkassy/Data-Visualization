from operator import itemgetter

import requests
# import plotly graph objects
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0),
    }
    submission_dicts.append(submission_dict)

# Sort the submissions by the number of comments.
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# Print the title, discussion link, and number of comments for each submission. (Optional)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


# Make visualization.
titles, num_comments, discussion_links = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict["title"]
    discussion_link = submission_dict["hn_link"]
    num_comment = submission_dict["comments"]

    titles.append(title)
    num_comments.append(num_comment)
    discussion_links.append(discussion_link)

data = [{
    "type": "bar",
    "x": titles,
    "y": num_comments,
    "marker": {
        "color": "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
    },
    "opacity": 0.6,
}]

my_layout = {
    "title": "Most active discussions on Hacker News",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Article",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Number of comments",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="data/hn_discussions.html")
