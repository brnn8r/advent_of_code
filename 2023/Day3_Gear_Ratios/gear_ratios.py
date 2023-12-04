import sys
sys.path.append('../utils')

from input_loader import InputLoader
from uuid import uuid4

def is_symbol(input: str) -> bool:
    return input != '.' and not input.isnumeric()

def parse_line(line: str) -> list[str]:
    parsed_line = []
    digit_buffer = []

    for char in line:
        if char.isnumeric():
            digit_buffer.append(char)
        else:
            if digit_buffer:
                part_number_id = uuid4()
                for _ in digit_buffer:
                    parsed_line.append(("".join(digit_buffer), str(part_number_id)))
                digit_buffer = []

            parsed_line.append(char)

    return parsed_line

def cube_conundrum():
    print("Day3: Gear Ratios")

    data = InputLoader().get_input_lines()

    data_matrix = [parse_line(line) for line in data]

    part_numbers = []
    part_uuids = []

    for row_number, row in enumerate(data_matrix):

        for column_number, value in enumerate(row):
            if type(value) is not tuple:
                continue

            _, part_id = value

            part_uuids.append(part_id)

            try:
                if is_symbol(data_matrix[row_number - 1][column_number - 1]):
                    part_numbers.append(value)
                    continue
            except:
                pass

            try:
                if is_symbol(data_matrix[row_number - 1][column_number]):
                    part_numbers.append(value)
                    continue
            except:
                pass

            try:
                if is_symbol(data_matrix[row_number - 1][column_number + 1]):
                    part_numbers.append(value)
                    continue
            except:
                pass

            try:
                if is_symbol(data_matrix[row_number][column_number + 1]):
                    part_numbers.append(value)
                    continue
            except:
                pass

            try:
                if is_symbol(data_matrix[row_number + 1][column_number + 1]):
                    part_numbers.append(value)
                    continue
            except:
                pass

            try:
                if is_symbol(data_matrix[row_number + 1][column_number]):
                    part_numbers.append(value)
                    continue
            except:
                pass

            try:
                if is_symbol(data_matrix[row_number + 1][column_number - 1]):
                    part_numbers.append(value)
                    continue
            except:
                pass

            try:
                if is_symbol(data_matrix[row_number][column_number - 1]):
                    part_numbers.append(value)
                    continue
            except:
                pass

    print(part_numbers)
    de_duplicated_parts = []
    for part_id in set(part_uuids):
        de_duplicated_parts.append(next((part for part in part_numbers if part[1] == part_id), None))
        de_duplicated_parts = [part for part in de_duplicated_parts if part]


    de_duplicated_part_ids =set([part[0] for part in de_duplicated_parts])

    print(de_duplicated_part_ids)

    for part_id in de_duplicated_part_ids:
        print(part_id)

    print(f"Sum of part numbers: {sum([int(part_id) for part_id in de_duplicated_part_ids])}")


if __name__ == "__main__":
    cube_conundrum()
