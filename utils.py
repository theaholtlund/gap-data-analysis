# Utilities for Data Analytics Framework for GAP Package Management

# Import required libraries and packages
import os
from pathlib import Path
from github import Github

# Define function to authorise a user with their GitHub token
def get_github_token():
    token_file_path = os.path.expanduser('~/.github_token')

    try:
        with open(token_file_path, 'r') as token_file:
            github_token = token_file.read().strip()
        return github_token
    except FileNotFoundError:
        print(f"GitHub token file does not exist in '{token_file_path}'.")
    except Exception as exception:
        print(f"Error reading GitHub token file: {str(exception)}")

