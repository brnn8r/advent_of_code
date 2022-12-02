from hand_gestures import Rock, Paper, Scissors


def create_hand_gesture(symbol):
    if symbol in ['A', 'X']:
        return Rock()
    elif symbol in ['B', 'Y']:
        return Paper()
    elif symbol in ['C', 'Z']:
        return Scissors()
    else:
        raise ValueError(f"unknown hand gesture {symbol}")
