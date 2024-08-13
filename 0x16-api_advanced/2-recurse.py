#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, including pagination and limit
    params = {"after": after} if after else {}
    # Send GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates success
    if response.status_code == 200:
        # Parse the JSON response and extract relevant data
        results = response.json()
        posts = data['data']['children']

        # Return none if post is not found
        if not posts:
            return None
        # Extract titles
        titles = [post['data']['title'] for post in posts]

        # Check more post
        after = data['data'].get('after')
        if after:
        #Recursively fetch more post
            titles += fetch_hot_titles(subreddit, after)
        return titles
    else:
        return None
