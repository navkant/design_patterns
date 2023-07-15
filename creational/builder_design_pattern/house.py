class House:
    def __init__(
        self,
        building_type="Apartment",
        doors=0,
        windows=0,
        wall_material="Brick",
    ):
        self.building_type = building_type
        self.doors = doors
        self.windows = windows
        self.wall_material = wall_material

    def construction(self):
        return f"This is a {self.wall_material} " \
               f"{self.building_type} with {self.doors} " \
               f"door(s) and {self.windows} window(s)"
