# Import required libraries, modules and packages
from github import Github
from setup.utils import *

# Get GitHub access token and create instance of the GitHub class
github_token = get_github_token()
if github_token:
    g = Github(github_token)
