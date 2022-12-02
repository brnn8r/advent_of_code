from typing import List
from utils import chunk_list
from backpack import Backpack
from food_item import FoodItem


class BackpackLoader:
    def __init__(self, backpack_file_path: str):
        self._backpack_file_path = backpack_file_path
    def generate_backpack(self) -> List[Backpack]:
        with open(self._backpack_file_path) as backpack_file:
            lines = backpack_file.readlines()

        backpacks = []
        for backpack_items in chunk_list(lines, "\n"):
            backpack = Backpack()
            for item in backpack_items:
                food_item = FoodItem(item)
                backpack.add_item(food_item)

            backpacks.append(backpack)

        return backpacks

