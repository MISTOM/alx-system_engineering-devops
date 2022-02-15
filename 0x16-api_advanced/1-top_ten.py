#!/usr/bin/python3
'''
a function that queries the Reddit API
and prints the titles of the first
10 hot posts listed for a given subreddit.
'''

import requests


def top_ten(subreddit):
    '''
    queries the Reddit API
    titles of the first
    10 hot posts listed
    '''
    if subreddit is None or type(subreddit) is not str:
        print(None)
    headers = {
        'User-Agent': 'Python/requests:api.advanced:v1.0.0 (by /u/kigarde)'
    }
    params = {
        'limit': 10
    }
    RequestData = requests.get(
        'http://www.reddit.com/r/{}/hot.json'.format(
            subreddit
        ),
        headers=headers,
        params=params
    ).json()
    posts = RequestData.get(
        'data',
        {}
    ).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get('title', None))
