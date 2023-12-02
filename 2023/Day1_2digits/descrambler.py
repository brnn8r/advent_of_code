import sys
sys.path.append('../utils')

from input_loader import InputLoader

def descramble():
    print("Day1: Descramble")

    input = InputLoader().get_input_lines()

    running_total = 0

    for line in input:
        line_digits = [int(i) for i in line if i.isdigit()]
        running_total += int(f"{line_digits[0]}{line_digits[-1]}")

    print(running_total)

if __name__ == "__main__":
    descramble()
