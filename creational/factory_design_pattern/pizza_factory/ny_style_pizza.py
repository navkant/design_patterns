from pizza_abstract_class import PizzaAbstractClass


class NYStyleCheesePizza(PizzaAbstractClass):
    def __init__(self):
        self.name = "NY style sauce and cheese pizza"
        self.dough = "Thin crust dough"
        self.sauce = "Mariana sauce"
        self.toppings.append("Grated Raggiano Cheese")
