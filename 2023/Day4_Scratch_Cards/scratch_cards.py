import math
import sys
sys.path.append('../utils')

import copy
from input_loader import InputLoader
import itertools
import more_itertools
from card_game import CardGame


def scratch_cards():
    print("Day4: Scratch Cards")

    data = InputLoader().get_input_lines()

    card_games = [parse_card_game(line) for line in data]

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

def parse_card_game(card_line: str) -> CardGame:
    split_card_line = card_line.split(":")

    card_id = int(split_card_line[0].replace("Card","").replace(" ",""))

    trimmed_card_line_ex_game = [s.strip() for s in "".join(split_card_line[1:]).split("|")]

    card_numbers = set(trimmed_card_line_ex_game[0].split())
    drawn_numbers = set(trimmed_card_line_ex_game[1].split())

    return CardGame(card_id, card_numbers, drawn_numbers)

    #return  card_numbers, drawn_numbers


if __name__ == "__main__":
    scratch_cards()
