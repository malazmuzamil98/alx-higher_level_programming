#!/usr/bin/python3
"""
Script that retrieves and prints the 10 most recent commits
(from the most recent to oldest) of a given repository by a specified
owner using the GitHub API.
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f'{sha}: {author}')
    else:
        print("Error:", response.status_code)
