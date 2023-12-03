from typing import List
from dataclasses import dataclass
from itertools import batched


@dataclass
class CubeGame:
    MAX_RED_CUBES = 12
    MAX_GREEN_CUBES = 13
    MAX_BLUE_CUBES = 14

    game_id: int
    max_drawn_red_cubes: int
    max_drawn_green_cubes: int
    max_drawn_blue_cubes: int

    def is_valid_game(self) -> bool:
        return self.max_drawn_red_cubes <= self.MAX_RED_CUBES and self.max_drawn_green_cubes <= self.MAX_GREEN_CUBES and self.max_drawn_blue_cubes <= self.MAX_BLUE_CUBES

    def power(self) -> int:
        return self.max_drawn_red_cubes * self.max_drawn_green_cubes * self.max_drawn_blue_cubes


def parse_game(game_info: str) -> CubeGame:
    game_id = 0
    red_cubes = 0
    green_cubes = 0
    blue_cubes = 0

    scrubbing_table = str.maketrans('', '', ';,:')

    cleaned_game_info = game_info.translate(scrubbing_table).lower()

    game_tokens = create_tokens(cleaned_game_info)

    for token in game_tokens:
        if token[0] == 'game':
            game_id = int(token[1])
        elif token[1] == 'red':
            red_cubes = max(red_cubes, int(token[0]))
        elif token[1] == 'green':
            green_cubes = max(green_cubes,int(token[0]))
        elif token[1] == 'blue':
            blue_cubes = max(blue_cubes,int(token[0]))
        else:
            raise ValueError(f"{token} is invalid")

    return CubeGame(game_id, red_cubes, green_cubes, blue_cubes)


def create_tokens(game_info: str) -> List[str]:
    sub_tokens = game_info.split()

    return list(batched(sub_tokens, 2))

