#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and retrieves a list of hot article titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to accumulate the titles of hot articles. Defaults to an empty list.

    Returns:
        list: List of hot article titles.
            Returns None if no results are found or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100}  # Set the maximum number of articles per request

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']

        for child in children:
            title = child['data']['title']
            hot_list.append(title)

        if data['data']['after'] is not None:
            params['after'] = data['data']['after']
            recurse(subreddit, hot_list)  # Recursive call with the 'after' parameter
        else:
            return hot_list
    else:
        return None
