from enum import Enum
from hand_gestures import HandGesture


class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


def calculate_result_value(opponent_hand_gesture: HandGesture, your_hand_gesture: HandGesture):
    return your_hand_gesture.value + calulate_result(opponent_hand_gesture, your_hand_gesture).value


def calulate_result(opponent_hand_gesture: HandGesture, your_hand_gesture: HandGesture):
    if opponent_hand_gesture == your_hand_gesture:
        return Result.DRAW
    elif your_hand_gesture.beats() == opponent_hand_gesture:
        return Result.WIN
    elif your_hand_gesture.beaten_by() == opponent_hand_gesture:
        return Result.LOSE
    else:
        raise ValueError("This shouldn't happen :)")
