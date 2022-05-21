#!/usr/bin/python3
"""
    function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """take the firt 10 items"""

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = requests.get(url, headers=headers).json()
    ten = req.get('data', {}).get('children', [])
    if not ten:
        print(None)
    for t in ten:
        print(t.get('data').get('title'))
