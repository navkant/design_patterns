import abc
from typing import List


class PizzaAbstractClass(abc.ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str] = []

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings...")
        for topping in self.toppings:
            print(f" {topping}")

    def bake(self) -> None:
        print(f"Bake for 25 mins at 350")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in the box")

    def get_name(self):
        return self.name
