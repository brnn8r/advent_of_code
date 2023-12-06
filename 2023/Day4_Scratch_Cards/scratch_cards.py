import math
import sys
sys.path.append('../utils')

import copy
from typing import List
from input_loader import InputLoader
from card_game import parse_card_game, CardGame


def scratch_cards():
    print("Day4: Scratch Cards")

    data = InputLoader().get_input_lines()

    card_games: List[CardGame] = [parse_card_game(line) for line in data]

    print(f"Part 1 Total scratch card points: {sum(card_game.card_points for card_game in card_games)}")

    cards_to_process = copy.deepcopy(card_games)
    processed_cards = []
    count = 0

    while cards_to_process:
        count += 1
        card = cards_to_process[0]

        len_winning_numbers = len(card.winning_numbers)
        if len_winning_numbers > 0:
            new_cards = [new_card for new_card in card_games if card.id < new_card.id <= card.id + len_winning_numbers]

            for new_card in new_cards:
                cards_to_process.append(new_card)

        if count % 100000 == 0:
            print(f"processed card id: {card.id}")
            print(f"# winning numbers: {len_winning_numbers}")
            #print(f"processed cards: {more_itertools.ilen(processed_cards)}")
            print(f"remaining cards to process: {len(cards_to_process)}")

        processed_cards.append(card)
        cards_to_process.pop(0)

    print(f"Total number of scratch cards: {len(processed_cards)}")



if __name__ == "__main__":
    scratch_cards()
