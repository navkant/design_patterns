from beverage_abstract_class import BeverageAbstractClass


class Espresso(BeverageAbstractClass):
    description = "Espresso"

    def cost(self) -> float:
        return 1.99
