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