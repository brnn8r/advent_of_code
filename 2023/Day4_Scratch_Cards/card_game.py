import math
from typing import Set
from dataclasses import dataclass
@dataclass
class CardGame:

    id: int
    card_numbers: Set[int]
    drawn_numbers: Set[int]

    def __post_init__(self):
        self._winning_numbers = self.card_numbers & self.drawn_numbers

    @property
    def winning_numbers(self) -> Set[int]:
        return self._winning_numbers

    @property
    def card_points(self) -> int:
        if not self.winning_numbers:
            return 0

        return int(math.pow(2, len(self.winning_numbers) - 1))


def parse_card_game(card_line: str) -> CardGame:
    split_card_line = card_line.split(":")

    card_id = int(split_card_line[0].replace("Card","").replace(" ",""))

    trimmed_card_line_ex_game = [s.strip() for s in "".join(split_card_line[1:]).split("|")]

    card_numbers = set(trimmed_card_line_ex_game[0].split())
    drawn_numbers = set(trimmed_card_line_ex_game[1].split())

    return CardGame(card_id, card_numbers, drawn_numbers)