from typing import List
from dataclasses import dataclass

@dataclass
class CategoryMap:
    name: str
    source_start: int
    destination_start: int
    range: int

@dataclass
class CategoryLookup:
    categoryMaps: List[CategoryMap]

    def map(self, source_id):
        for map in self.categoryMaps:
            if map.source_start <= source_id <= map.source_start + map.range:
                # i.e. add the offset of the source_id from the source start to the destination start
                destination_id = map.destination_start + (source_id - map.source_start)
                #print(map)
                #print(f"{source_id}->{destination_id}")
                return destination_id

        #not in the map so source_id == destination_id
        #print(f"{source_id}->{source_id}")
        return source_id


def parse_category_map(name: str, input: str) -> CategoryMap:
    category_parts = input.split(" ")

    return CategoryMap(name, int(category_parts[1]),int(category_parts[0]), int(category_parts[2]))