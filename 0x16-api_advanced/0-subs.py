#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """get number of subscribers"""
    user_agent = {'User-agent': 'Ayomide'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    raw_data = requests.get(url, headers=user_agent, allow_redirects=False)
    result = raw_data.json()
    if raw_data.status_code != 200:
        return 0
    result = raw_data.json()
    if 'data' not in result:
        return 0
    if 'subscribers' not in result.get('data'):
        return 0
    result(result['data']['subscribers'])
