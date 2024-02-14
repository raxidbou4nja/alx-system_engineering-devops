#!/usr/bin/python3
"""
Query Reddit API and return the total number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        get number of subscribers for a given subreddit
        return 0 if invalid subreddit given
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
