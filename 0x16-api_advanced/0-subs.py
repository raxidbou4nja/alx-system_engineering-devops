#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'by /u/factos22'}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        data = r.json()
        subs = data.get("data", {}).get("subscribers", 0)
        return subs
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
