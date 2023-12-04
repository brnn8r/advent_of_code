from typing import List


class InputLoader:
    @staticmethod
    def get_default_path():
        return "input.txt"

    def __init__(self, input_path: str = ""):
        self.input_path = input_path or self.get_default_path()
        self.input_lines = []

    def get_input_lines(self) -> List[str]:
        if not self.input_lines:
            with open(self.input_path) as input_file:
                self.input_lines = input_file.read().splitlines()

        return self.input_lines