from typing import List
from dataclasses import dataclass

@dataclass
class ToyBoat:
    velocity: int

    def distance_travelled(self, time: int) -> int:
        return self.velocity * time