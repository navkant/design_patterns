from beverage_abstract_class import BeverageAbstractClass


class DarkRoast(BeverageAbstractClass):
    description = "Dark Roast"

    def cost(self) -> float:
        return 0.99
