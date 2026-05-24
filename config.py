import json
import os

DEFAULT_CONFIG = {
    'screen_width': 1920,
    'screen_height': 1080,
    'fullscreen': False,
    'volume': 50,
    'controls': {
        'move_left': 'A',
        'move_right': 'D',
        'jump': 'SPACE',
        'shoot': 'LEFT_MOUSE'
    }
}

def load_config(file_path):
    """Load configuration from a JSON file and merge with defaults."""
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as f:
        user_config = json.load(f)
    merged_config = {**DEFAULT_CONFIG, **user_config}
    return merged_config
