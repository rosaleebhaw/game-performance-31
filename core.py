import random
import sys

class GameError(Exception):
    pass

class Game:
    def __init__(self, players):
        if not isinstance(players, int) or players <= 0:
            raise GameError('Number of players must be a positive integer.')
        self.players = players
        self.scores = [0] * players

    def play_round(self):
        try:
            for i in range(self.players):
                score = random.randint(1, 10)
                self.scores[i] += score
                print(f'Player {i + 1} scored {score}. Total: {self.scores[i]}')
        except Exception as e:
            print(f'An error occurred during the round: {e}')
            sys.exit(1)

    def get_winner(self):
        if all(s == 0 for s in self.scores):
            raise GameError('No scores to determine a winner.')
        winner = self.scores.index(max(self.scores)) + 1
        return winner

if __name__ == '__main__':
    try:
        num_players = int(input('Enter number of players: '))
        game = Game(num_players)
        for _ in range(5):
            game.play_round()
        winner = game.get_winner()
        print(f'The winner is Player {winner}.')
    except GameError as e:
        print(f'Game Error: {e}')
    except ValueError:
        print('Please enter a valid integer for number of players.')