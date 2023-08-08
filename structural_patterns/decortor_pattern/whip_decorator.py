from condiment_decorator_abstract_class import CondimentDecorator
from beverage_abstract_class import BeverageAbstractClass


class Whip(CondimentDecorator):
    beverage: BeverageAbstractClass

    def __init__(self, beverage: BeverageAbstractClass):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", whip"

    def cost(self) -> float:
        return 0.2 + self.beverage.cost()
