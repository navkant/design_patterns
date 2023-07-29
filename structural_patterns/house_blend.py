from beverage_abstract_class import BeverageAbstractClass


class HouseBlend(BeverageAbstractClass):
    description = "House blend coffee"

    def cost(self) -> float:
        return 0.89
