from hand_gestures import Rock, Paper, Scissors
from result_calculator import calculate_result_value


def rock_paper_scissors():
    opponent_hand_gesture = Rock()
    your_hand_gesture = Paper()

    print(calculate_result_value(opponent_hand_gesture, your_hand_gesture))


if __name__ == "__main__":
    rock_paper_scissors()
