#!/usr/bin/python3
"""
    Write a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit
"""
from requests import get
after = ''


def recurse(subreddit, hot_list=[]):
    """recursive function"""
    global after
    header = {'User-Agent': 'My User Agent 1.0'}
    try:
        url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
        if after:
            url = url + '?after={}'.format(after)
        getting = get(url, headers=header, allow_redirects=False).json()
        for children in getting['data']['children']:
            hot_list.append(children.get('data').get('title'))
        after = get(url, headers=header,
                    allow_redirects=False).json().get('data').get('after')
        if after:
            return recurse(subreddit, hot_list)
        return hot_list
    except:
        return None
