import sys
sys.path.append('../utils')

from input_loader import InputLoader
from cube_game import CubeGame, parse_game

def cube_conundrum():
    print("Day2: Cube Conundrum")

    data = InputLoader().get_input_lines()

    valid_games = [parse_game(line).game_id for line in data if parse_game(line).is_valid_game()]

    print(f"valid games: {valid_games}, sum of these ids: {sum(valid_games)}")

if __name__ == "__main__":
    cube_conundrum()
