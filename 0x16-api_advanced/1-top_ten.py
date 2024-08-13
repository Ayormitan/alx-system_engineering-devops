#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    # Check if the response status code is successful
    if response.status_code == 200:
        results = response.json()
        posts = results['results']['children'][:10]
        # Print the titles of the top 10 hottest posts
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")
