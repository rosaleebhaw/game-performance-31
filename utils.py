import time

def timeit(func):
    """Decorator to measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@timeit
def optimize_heavy_computation(data):
    """Example function for heavy computation optimization."""
    return [x * 2 for x in data if x % 2 == 0]

@timeit
def fetch_and_process_data(data_source):
    """Fetch data from a source and process it efficiently."""
    data = data_source.fetch()
    processed_data = optimize_heavy_computation(data)
    return processed_data

if __name__ == '__main__':
    class MockDataSource:
        def fetch(self):
            return list(range(1000000))

    data_source = MockDataSource()
    fetch_and_process_data(data_source)