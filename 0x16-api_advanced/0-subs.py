#!/usr/bin/python3
""" a function that queries the Reddit API and
    returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    req = requests.get(url, headers=headers).json()
    subscriber = req.get('data', {}).get('subscribers')
    if not subscriber:
        return 0
    return subscriber
