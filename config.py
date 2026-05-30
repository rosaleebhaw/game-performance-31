import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config_data = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.filepath):
            raise ConfigError(f'Config file not found: {self.filepath}')
        try:
            with open(self.filepath, 'r') as config_file:
                self.config_data = json.load(config_file)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from config file')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def set(self, key, value):
        self.config_data[key] = value

    def save(self):
        try:
            with open(self.filepath, 'w') as config_file:
                json.dump(self.config_data, config_file, indent=4)
        except Exception as e:
            raise ConfigError(f'Error saving config file: {str(e)}')
