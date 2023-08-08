from beverage_abstract_class import BeverageAbstractClass
from espresso_beverage import Espresso
from dark_roast_beverage import DarkRoast
from house_blend import HouseBlend
from mocha_decorator import Mocha
from whip_decorator import Whip


def main():
    beverage: BeverageAbstractClass = Espresso()
    print(f"{beverage.get_description()} - {beverage.cost()}")
    print("******")
    beverage_2: BeverageAbstractClass = DarkRoast()
    beverage_2 = Mocha(beverage_2)
    print(f"{beverage_2.get_description()} - {beverage_2.cost()}")
    print("******")
    beverage_3: BeverageAbstractClass = HouseBlend()
    beverage_3 = Mocha(beverage_3)
    beverage_3 = Mocha(beverage_3)
    beverage_3 = Whip(beverage_3)
    print(f"{beverage_3.get_description()} - {beverage_3.cost()}")


if __name__ == "__main__":
    main()
