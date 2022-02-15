#!/usr/bin/python3
'''
a recursive function that queries
the Reddit API and returns a list
containing the titles of all hot
articles for a given subreddit.
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    queries
    the Reddit API and returns a list
    containing the titles of all hot
    posts
    '''
    if subreddit is None or type(subreddit) is not str:
        return None
    headers = {
        'User-Agent': 'Python/requests:api.advanced:v1.0.0 (by /u/kigarde)'
    }
    params = {
        "after": after,
        "limit": 100
    }
    RequestData = requests.get(
        "http://www.reddit.com/r/{}/hot.json".format(
            subreddit
        ),
        headers=headers,
        params=params
    ).json()
    after = RequestData.get(
        'data', {}
    ).get(
        'after', None
    )
    posts = RequestData.get(
        'data', {}
    ).get(
        'children', None
    )
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
