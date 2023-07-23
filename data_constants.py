# Defining constants for Data Analytics Framework for GAP Package Management

# Import modules and modules from other project scripts
from setup.config import *
import time
from datetime import datetime

# Constants for organisation
ORG_NAME_PACKAGES = "gap-packages"
ORG_NAME_SYSTEM = "gap-system"

# Constants for repositories
DISTRO_REPO = "PackageDistro"

def wait_until_reset(reset_time: str) -> None:
    """Wait until the GitHub API rate limit resets by calculating the time difference between
    the current time and the provided reset time. If the reset time is in the future, it sleeps for the time difference.

    Args:
        reset_time (str): The reset time of the GitHub API rate limit in the format '%Y-%m-%d %H:%M:%S'.

    Returns:
        None        
    """

    # Calculate the time difference between current time and reset time
    current_time = datetime.now()
    time_difference = reset_time - current_time

    # Sleep only if the reset time is in the future
    if time_difference.total_seconds() > 0:
        sleep_time = time_difference.total_seconds()
        sleep_time_minutes = sleep_time / 60
        print(f"Reached GitHub API rate limit. Sleeping for {sleep_time_minutes} seconds until the limit resets.")
        time.sleep(sleep_time)