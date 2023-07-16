from house_builder import HouseBuilder


class IglooDirector:
    def construct(self):
        """Constructs and returns the final product
        Note that in this IglooDirector, it has omitted the set_number_of_windows
        call since this Igloo will have no windows"""
        return HouseBuilder()\
            .set_building_type("Igloo")\
            .set_wall_material("Ice")\
            .set_number_of_doors(1)\
            .get_result()
