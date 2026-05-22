import os
import json


def load_json(file_path):
    """
    Load a JSON file and return its content.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    """
    Save data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_game_data(directory):
    """
    Retrieve all JSON game data files from a given directory.
    """
    game_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            game_data.append(load_json(file_path))
    return game_data


def format_game_data(data):
    """
    Transform game data into a readable format.
    """
    formatted_data = []
    for game in data:
        formatted_data.append(f"{game.get('title')} - {game.get('genre')} - {game.get('release_date')}")
    return formatted_data
