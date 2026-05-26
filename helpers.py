import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, delay=2):
    """
    Perform a GET request with retry logic.
    Retries up to max_retries times in case of failure.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming we want JSON response
        except requests.RequestException as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts < max_retries:
                time.sleep(delay)  # wait before retrying
            else:
                raise NetworkError(f'Failed to fetch data after {max_retries} attempts')

# Example usage:
# data = retry_request('https://api.example.com/data')