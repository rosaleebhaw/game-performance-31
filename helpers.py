import random
import numpy as np

def generate_random_levels(level_count: int, min_difficulty: int, max_difficulty: int) -> list:
    levels = []
    for _ in range(level_count):
        difficulty = random.randint(min_difficulty, max_difficulty)
        levels.append(difficulty)
    return levels


def calculate_average_difficulty(levels: list) -> float:
    if not levels:
        return 0.0
    return sum(levels) / len(levels)


def improve_difficulty(levels: list, increase_by: int) -> list:
    return [min(difficulty + increase_by, 100) for difficulty in levels]


def generate_enemy_stats(levels: list) -> dict:
    enemy_stats = {}
    for level in levels:
        enemy_stats[level] = {
            'health': np.random.randint(50, 150) + level * 10,
            'attack': np.random.randint(5, 20) + level,
            'defense': np.random.randint(5, 15) + level // 2,
        }
    return enemy_stats


def display_stats(enemy_stats: dict) -> None:
    for level, stats in enemy_stats.items():
        print(f'Level {level} => Health: {stats['health']}, Attack: {stats['attack']}, Defense: {stats['defense']}')
