from hand_gestures import HandGesture, Rock, Paper, Scissors


def obsolete_create_hand_gesture(symbol):
    if symbol in ['A', 'B', 'C']:
        return create_hand_gesture(symbol)
    elif symbol == 'X':
        return Rock()
    elif symbol == 'Y':
        return Paper()
    elif symbol == 'Z':
        return Scissors()
    else:
        raise ValueError(f"unknown hand gesture {symbol}")


def create_hand_gesture(symbol):
    if symbol == 'A':
        return Rock()
    elif symbol == 'B':
        return Paper()
    elif symbol == 'C':
        return Scissors()
    else:
        raise ValueError(f"unknown hand gesture {symbol}")


def create_expected_hand_gesture(gesture: HandGesture, symbol):
    if symbol == 'X':
        return gesture.beats()
    elif symbol == 'Y':
        return gesture
    elif symbol == 'Z':
        return gesture.beaten_by()
