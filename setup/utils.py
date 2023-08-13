# Utilities for Data Analytics Framework for GAP Package Management

# Import required libraries and packages
import os
import time
from pathlib import Path
from github import Github
from datetime import datetime

# Get the GitHub token and set it for the environment
def get_github_token() -> str:
    """Get the GitHub token for user authorisation.

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
    # For Docker, first check if GitHub token is set as environment variable
    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token != 'YOUR_GITHUB_TOKEN':
        return github_token
    
    # If no environment variable, access GitHub token from home dir
    token_file_path = os.path.expanduser('~/.github_shell_token')
    try:
        with open(token_file_path, 'r') as token_file:
            github_token = token_file.read().strip()
        return github_token
    except FileNotFoundError:
        print(f"GitHub token file does not exist in '{token_file_path}'.")
    except Exception as exception:
        print(f"Error reading GitHub token file: {str(exception)}")

# Sleep function to pause data extraction process if API calls run out
def wait_until_reset(reset_time: int) -> None:
    """Wait until the GitHub API rate limit resets by calculating the time difference between
    the current time and the provided reset time. If the reset time is in the future, it sleeps for the time difference.

    Args:
        reset_time (int): The reset time of the GitHub API rate limit in UNIX timestamp format.

    Returns:
        None        
    """

    # Convert UNIX timestamp to a datetime object
    reset_datetime = datetime.fromtimestamp(reset_time)

    # Calculate the time difference between current time and reset time
    current_time = datetime.now()
    time_difference = reset_datetime - current_time

    # Sleep only if the reset time is in the future
    if time_difference.total_seconds() > 0:
        sleep_time = time_difference.total_seconds()
        sleep_time_minutes = sleep_time / 60
        print(f"Reached GitHub API rate limit. Sleeping for {sleep_time_minutes} minutes until the limit resets.")
        time.sleep(sleep_time)
