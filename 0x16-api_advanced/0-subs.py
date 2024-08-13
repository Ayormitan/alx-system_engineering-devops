#!/usr/bin/python3
"""
Script/function that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    """ Define the API endpoint"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    """ Set the header """
    headers = {"User-Agent": "Mozilla/5.0"}
    """ Make a GET request to Reddit API"""
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        """ Parse the Json response"""
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
