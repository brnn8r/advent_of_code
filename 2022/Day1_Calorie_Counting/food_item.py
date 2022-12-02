from dataclasses import dataclass
@dataclass()
class FoodItem:
    calories: int
    def __post_init__(self):
        self.calories = int(self.calories)
