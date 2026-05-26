import json
import os

DEFAULT_CONFIG = {
    'screen_width': 1920,
    'screen_height': 1080,
    'fullscreen': False,
    'volume': 75,
    'difficulty': 'normal'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    config = json.load(file)
                    return {**DEFAULT_CONFIG, **config}
                except json.JSONDecodeError:
                    print(f"Error loading config: {self.config_file}")
                    return DEFAULT_CONFIG
        else:
            print(f"Config file not found, using defaults.")
            return DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)  # Display loaded configuration
