from typing import List
from dataclasses import dataclass

CARD_STRENGTH = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
    "J": 14
}

@dataclass
class Card:
    value: str

    @property
    def strength(self):
        return CARD_STRENGTH[self.value]

