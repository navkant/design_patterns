from house_builder_concept import AbstractHouseBuilder
from house import House


class HouseBuilder(AbstractHouseBuilder):
    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def set_number_of_doors(self, number):
        self.house.doors = number
        return self

    def set_number_of_windows(self, number):
        self.house.windows = number
        return self

    def get_result(self):
        return self.house
