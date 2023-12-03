import sys

sys.path.append('../utils')

from input_loader import InputLoader

DIGIT_STRINGS = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def descramble():
    print("Day1: Trebuchet")

    data = InputLoader().get_input_lines()

    running_total = 0

    for line in data:
        print(line)
        parsed_line = digits_to_words(line)
        print(parsed_line)

        first_number = get_first_number(parsed_line)
        last_number = get_last_number(parsed_line)

        print(first_number, last_number)

        running_total += int(f"{first_number}{last_number}")

    print(f"Calibration value: {running_total}")


def get_first_number(line: str) -> int:
    min_pos = len(line)
    first_number = ""

    for num in DIGIT_STRINGS.keys():
        num_pos = line.find(num)
        if num_pos < min_pos and num_pos >= 0:
            first_number = num
            min_pos = num_pos

    return DIGIT_STRINGS[first_number]



def get_last_number(line: str) -> int:
    max_pos = -1
    last_number = ""

    for num in DIGIT_STRINGS.keys():
        num_pos = line.rfind(num)
        if num_pos > max_pos and num_pos >= 0:
            last_number = num
            max_pos = num_pos

    return DIGIT_STRINGS[last_number]

def digits_to_words(line: str) -> str:

    parsed_line = line.replace("1", "one" )
    parsed_line = parsed_line.replace("2", "two")
    parsed_line = parsed_line.replace("3", "three")
    parsed_line = parsed_line.replace("4", "four")
    parsed_line = parsed_line.replace("5", "five")
    parsed_line = parsed_line.replace( "6", "six")
    parsed_line = parsed_line.replace("7", "seven")
    parsed_line = parsed_line.replace("8", "eight")
    parsed_line = parsed_line.replace("9", "nine")

    return parsed_line

if __name__ == "__main__":
    descramble()
