def load_game_data(file_path):
    import json
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
        return None
    except json.JSONDecodeError:
        print('Error: Failed to decode JSON from the file')
        return None
    except Exception as e:
        print(f'Unexpected error: {e}')
        return None


def save_game_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except IOError:
        print(f'Error: Couldn't write to file at {file_path}')
    except Exception as e:
        print(f'Unexpected error: {e}')


def validate_game_score(score):
    if not isinstance(score, (int, float)):
        raise ValueError('Score must be an integer or float')
    if score < 0:
        raise ValueError('Score cannot be negative')
    return True


def handle_game_exception(exception):
    print(f'Game exception occurred: {exception}')
    # Additional logging can be implemented here