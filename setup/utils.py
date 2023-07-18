# Utilities for Data Analytics Framework for GAP Package Management

# Import required libraries and packages
import os
from pathlib import Path
from github import Github


def get_github_token() -> str:
    """Get the GitHub token for user authorization.

    Args:
        None

    Returns:
        str: The GitHub token.

    Raises:
        FileNotFoundError: If the GitHub token file does not exist.
        Exception: If there is an error reading the GitHub token file.

    Notes:
        This code was inspired by fingolfin's implementation in the gap-system repository:
        https://github.com/gap-system/gap/blob/master/dev/releases/utils.py
    """
    token_file_path = os.path.expanduser('~/.github_token')

    try:
        with open(token_file_path, 'r') as token_file:
            github_token = token_file.read().strip()
        return github_token
    except FileNotFoundError:
        print(f"GitHub token file does not exist in '{token_file_path}'.")
    except Exception as exception:
        print(f"Error reading GitHub token file: {str(exception)}")

