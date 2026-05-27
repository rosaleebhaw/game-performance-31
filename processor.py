import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_on_failure(max_attempts=3, delay=2):
    """Retry decorator for network operations."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts == max_attempts:
                        raise NetworkError(f"All {max_attempts} attempts failed.")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_on_failure(max_attempts=5, delay=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    try:
        data = fetch_data('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(f"Failed to fetch data: {e}")
