import sys
sys.path.append('../utils')

from input_loader import InputLoader
from cube_game import CubeGame, parse_game

def cube_conundrum():
    print("Day2: Cube Conundrum")

    data = InputLoader().get_input_lines()

    games = [parse_game(line) for line in data]

    valid_games = [game.game_id for game in games if game.is_valid_game()]

    print(f"valid games: {valid_games}, sum of these ids: {sum(valid_games)}")

    for game in games:
        print(game, game.power())

    print(f"Total games power: {sum(game.power() for game in games)}")



if __name__ == "__main__":
    cube_conundrum()
