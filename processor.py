import json
import logging
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_game_data(game_data: str) -> Dict[str, Any]:
    """Processes game data from a JSON string."""
    try:
        # Attempt to parse the JSON data
        data = json.loads(game_data)
    except json.JSONDecodeError as e:
        logger.error('Invalid JSON data: %s', e)
        return {'error': 'Invalid JSON format'}

    # Check required fields
    required_fields = ['game_id', 'score', 'player']
    for field in required_fields:
        if field not in data:
            logger.warning('Missing required field: %s', field)
            return {'error': f'Missing required field: {field}'}

    # Process game data
    try:
        result = {  
            'game_id': data['game_id'],  
            'score': data['score'],  
            'player': data['player'],  
        }
        logger.info('Successfully processed data for game_id: %s', data['game_id'])
        return result
    except Exception as e:
        logger.error('Error processing game data: %s', e)
        return {'error': 'Processing error', 'details': str(e)}

# Example usage (would be removed in production):
if __name__ == '__main__':
    example_data = '{"game_id": "1234", "score": 95, "player": "Player1"}'
    result = process_game_data(example_data)
    print(result)