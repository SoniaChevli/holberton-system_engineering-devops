#!/usr/bin/python3
'''
queries the Reddit API and
returns the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    URL = "https://www.reddit.com/r/{}/.json".format(subreddit)
    try:
        reddit_data = requests.get(url=URL, headers=headers)
        subscribers = reddit_data.json()\
                                 .get('data').\
                                 get('children')[0].\
                                 get('data').\
                                 get('subreddit_subscribers')
        return subscribers
    except:
        return 0
