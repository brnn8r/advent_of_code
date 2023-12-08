import sys
sys.path.append('../utils')

from input_loader import InputLoader
from typing import List
from hand import Hand, parse_hand, compare_hand
from functools import cmp_to_key

def camel_cards():
    print("Day7: Camel Cards")

    data = InputLoader("input.txt").get_input_lines()
    #print(data)

    hands : List[Hand] = [parse_hand(line) for line in data]

    sorted_hands = sorted(hands, key= cmp_to_key(compare_hand), reverse=True)

    total_winnings = 0
    for index, hand in enumerate(sorted_hands):
        total_winnings += (index+1) * hand.bid


    print(f"Total winnings: {total_winnings}")

if __name__ == "__main__":
    camel_cards()
