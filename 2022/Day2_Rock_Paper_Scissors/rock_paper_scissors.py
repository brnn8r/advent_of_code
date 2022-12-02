from hand_gestures import Rock, Paper, Scissors
from result_calculator import calculate_result_value
from hand_gesture_factory import obsolete_create_hand_gesture, create_hand_gesture, create_expected_hand_gesture

def rock_paper_scissors():
    input_file_path = "input.txt"

    with open(input_file_path) as input_file:
        game_rounds = input_file.readlines()

    total_score = 0
    for opponent_hand_gesture, your_hand_gesture in hydrate_game_rounds(game_rounds):
        score = calculate_result_value(opponent_hand_gesture, your_hand_gesture)
        total_score += score
        print(f"opponent does {opponent_hand_gesture}, you play {your_hand_gesture} and you score {score}, current total score is {total_score}")

def obsolete_hydrate_game_rounds(game_rounds):
    for game_round in game_rounds:
        opponent_hand_gesture, your_hand_gesture = ([obsolete_create_hand_gesture(gesture_symbol.strip()) for gesture_symbol in game_round.split(" ")])
        yield opponent_hand_gesture, your_hand_gesture

def hydrate_game_rounds(game_rounds):
    for game_round in game_rounds:
        opponent_hand_gesture_symbol, your_hand_gesture_symbol = ([gesture_symbol.strip() for gesture_symbol in game_round.split(" ")])
        opponent_hand_gesture = create_hand_gesture(opponent_hand_gesture_symbol)
        your_hand_gesture = create_expected_hand_gesture(opponent_hand_gesture, your_hand_gesture_symbol)
        yield opponent_hand_gesture, your_hand_gesture

if __name__ == "__main__":
    rock_paper_scissors()
