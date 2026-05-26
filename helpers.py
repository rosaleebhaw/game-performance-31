import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff=2):
    """Attempts to make a network request with retries on failure."""
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()  # Assuming we expect a JSON response
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(backoff ** attempt)  # Exponential backoff
            else:
                raise NetworkError(f"Failed to retrieve data after {retries} attempts.") from e

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as ne:
        print(ne)