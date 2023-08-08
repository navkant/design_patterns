import abc
from pizza_store_abstract_class import PizzaStoreAbstractClass
from pizza_abstract_class import PizzaAbstractClass
from ny_style_pizza import NYStyleCheesePizza


class NYPizzaStore(PizzaStoreAbstractClass):
    def order_pizza(self, type: str) -> PizzaAbstractClass:
        pizza: PizzaAbstractClass

        pizza = self.create_pizza(type="cheese")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def create_pizza(self, type: str):
        if type == "cheese":
            return NYStyleCheesePizza()
