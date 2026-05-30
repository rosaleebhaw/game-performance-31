import time
import requests

RETRY_COUNT = 3
WAIT_TIME = 2  # seconds


def retry_request(url, params=None):
    """
    Makes a network request with retry logic.
    Retries for a specified count with wait time between attempts.
    """
    attempt = 0
    while attempt < RETRY_COUNT:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON if request is successful
        except requests.exceptions.RequestException as e:
            print(f'Network error: {e}, attempt {attempt + 1} of {RETRY_COUNT}')
            attempt += 1
            time.sleep(WAIT_TIME)  # Wait before retrying
    raise Exception(f'Failed to retrieve data from {url} after {RETRY_COUNT} retries')
