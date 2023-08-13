# Configuration for Data Analytics Framework for GAP Package Management

# Import required libraries and packages
from github import Github

# Import modules from other project scripts
from setup.utils import *

# Get the GitHub access token and create instance of the GitHub class
github_token = get_github_token()
if github_token:
    g = Github(github_token)
