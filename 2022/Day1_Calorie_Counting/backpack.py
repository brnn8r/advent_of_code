from typing import List
from dataclasses import dataclass, field
from food_item import FoodItem


@dataclass
class Backpack:
    food_items: List[FoodItem] = field(default_factory=list)

    def add_item(self, item: FoodItem):
        self.food_items.append(item)

    def total_value(self):
        return sum([x.calories for x in self.food_items])
