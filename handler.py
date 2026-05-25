import time
import random

def process_game_event(event):
    if event['type'] == 'start':
        start_game(event['player'])
    elif event['type'] == 'end':
        end_game(event['player'], event['score'])
    else:
        print('Unknown event type')


def start_game(player):
    print(f'Starting game for {player}')
    player['active'] = True
    player['start_time'] = time.time()


def end_game(player, score):
    if player['active']:
        player['active'] = False
        duration = time.time() - player['start_time']
        print(f'Game ended for {player}. Score: {score}, Duration: {duration:.2f}s')
    else:
        print(f'{player} is not currently active.')


def generate_random_event():
    events = ['start', 'end']
    return {'type': random.choice(events), 'player': 'Player1', 'score': random.randint(0, 100)}


# Example usage of event processing
if __name__ == '__main__':
    for _ in range(5):
        event = generate_random_event()
        process_game_event(event)