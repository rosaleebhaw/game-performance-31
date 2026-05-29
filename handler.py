import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GameHandler:
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        if player_name:
            self.players.append(player_name)
            logger.info(f"Player {player_name} added.")
        else:
            logger.warning("Attempted to add an invalid player name.")

    def remove_player(self, player_name):
        try:
            self.players.remove(player_name)
            logger.info(f"Player {player_name} removed.")
        except ValueError:
            logger.warning(f"Player {player_name} not found in the list.")

    def get_player_list(self):
        return json.dumps(self.players)

if __name__ == '__main__':
    handler = GameHandler()
    handler.add_player('Alice')
    handler.add_player('Bob')
    print(handler.get_player_list())
    handler.remove_player('Alice')
    print(handler.get_player_list())
    handler.remove_player('Charlie')