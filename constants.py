from typing import Dict, Any

# Game configuration constants

# Player settings
PLAYER_HEALTH: int = 100
PLAYER_MANA: int = 50

# Game settings
GAME_TITLE: str = 'Epic Adventure'
GAME_VERSION: str = '1.0.0'

# Difficulty levels
DIFFICULTY: Dict[str, int] = {
    'easy': 1,
    'medium': 2,
    'hard': 3,
}

# Item types
ITEM_TYPES: Dict[str, Any] = {
    'weapon': {
        'damage': 15,
        'durability': 100,
    },
    'armor': {
        'defense': 10,
        'weight': 5,
    },
    'potion': {
        'healing': 20,
        'quantity': 5,
    },
}

# Other constants
MAX_PLAYERS: int = 10
MAX_LEVEL: int = 50

