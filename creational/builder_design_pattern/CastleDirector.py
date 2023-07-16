from house_builder import HouseBuilder


class CastleDirector:
    def construct(self):
        return HouseBuilder()\
            .set_building_type("Castle")\
            .set_wall_material("mortar")\
            .set_number_of_doors(20)\
            .set_number_of_windows(40)\
            .get_result()
