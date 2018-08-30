#!/usr/bin/python3
'''
queries the Reddit API and
returns the hot_list titles
'''
import requests


def recurse(subreddit, hot_list=[], index=0):
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    URL = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    try:
        reddit_data = requests.get(url=URL, headers=headers)
        all_data = reddit_data.json().get('data').get('children')

        if all_data[index].get('data').get('title'):
            hot_list.append(all_data[index].get('data').get('title'))
            return(recurse(subreddit, hot_list, index + 1))
    except:
        if len(hot_list) == 0:
            return None
        return hot_list
