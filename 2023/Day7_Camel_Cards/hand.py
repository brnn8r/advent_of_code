from dataclasses import dataclass
from typing import List
from card import Card
from itertools import groupby

HAND_STRENGTH = {
    "FIVE_OF_A_KIND": 1,
    "FOUR_OF_A_KIND": 2,
    "FULL_HOUSE": 3,
    "THREE_OF_A_KIND": 4,
    "TWO_PAIR": 5,
    "ONE_PAIR": 6,
    "HIGH_CARD": 7
}

@dataclass
class Hand:
    first_card: Card
    second_card: Card
    third_card: Card
    fourth_card: Card
    fifth_card: Card
    bid: int

    def __post_init__(self):
        self.cards = [self.first_card, self.second_card, self.third_card, self.fourth_card, self.fifth_card]

        card_counts = {key: len(list(group)) for key, group in groupby(sorted(self.cards, key=lambda card: card.value, reverse=True), key=lambda card: card.value)}
        self.hand_partition = dict(sorted(card_counts.items(), key=lambda item: item[1], reverse=True))
        self.hand_strength = self._calculate_hand_strength(list(self.hand_partition.items()))

    def _calculate_hand_strength(self, card_counts) -> int:
        print(card_counts)
        hand_name: str

        jacks_out_cards = []
        for index, card in enumerate(card_counts):
            if len(card_counts) == 1:
                jacks_out_cards.append(card)
            # we have jacks as our most common card but not all jacks
            elif index == 0 and card[0] == "J":
                jacks_out_cards.append( (card_counts[1][0], card_counts[1][1] + card[1]))
            elif card[0] == "J":
                jacks_out_cards[0] = (card_counts[0][0], card_counts[0][1] + card[1])
            else:
                jacks_out_cards.append(card)

        first_jacks_out_card = jacks_out_cards[0]

        if first_jacks_out_card[1] == 5:
            hand_name = "FIVE_OF_A_KIND"

        elif first_jacks_out_card[1] == 4:
            hand_name ="FOUR_OF_A_KIND"

        elif first_jacks_out_card[1] == 3 and jacks_out_cards[1][1] == 2:
            hand_name ="FULL_HOUSE"

        elif first_jacks_out_card[1] == 3:
            hand_name ="THREE_OF_A_KIND"

        elif first_jacks_out_card[1] == 2 and jacks_out_cards[1][1] == 2:
            hand_name ="TWO_PAIR"

        elif first_jacks_out_card[1] == 2:
            hand_name ="ONE_PAIR"

        else:
            hand_name ="HIGH_CARD"

        #print(hand_name)
        return HAND_STRENGTH[hand_name]


def parse_hand(input_line: str) -> Hand:
    split_line = input_line.split(" ")
    cards = split_line[0]
    bid = split_line[1]

    return Hand(Card(cards[0]), Card(cards[1]), Card(cards[2]), Card(cards[3]), Card(cards[4]), int(bid))


def compare_hand(first_hand, second_hand) -> int:
    if first_hand.hand_strength < second_hand.hand_strength:
        return -1

    if first_hand.hand_strength > second_hand.hand_strength:
        return 1

    for index, card in enumerate(first_hand.cards):
        if card.strength < second_hand.cards[index].strength:
            return -1
        if card.strength > second_hand.cards[index].strength:
            return 1

    return 0
