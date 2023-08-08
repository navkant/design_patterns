import abc
from pizza_abstract_class import PizzaAbstractClass


class PizzaStoreAbstractClass(abc.ABC):

    def order_pizza(self, type: str) -> PizzaAbstractClass:
        pizza: PizzaAbstractClass

        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abc.abstractmethod
    def create_pizza(self, type: str):
        pass
