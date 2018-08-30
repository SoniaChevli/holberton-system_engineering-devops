#!/usr/bin/python3
'''
queries the Reddit API and
returns the number of subscribers
'''
import requests


def top_ten(subreddit):
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    URL = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    try:
        reddit_data = requests.get(url=URL, headers=headers)
        all_data = reddit_data.json().get('data').get('children')
        print('a')
        titles = []
        print('b')
        for i in all_data:
            if i.get('data').get('title'):
                titles.append(i.get('data').get('title'))

            print(i)
        print('c')
        for t in titles:
            print(t)
    except:
        print('None')
