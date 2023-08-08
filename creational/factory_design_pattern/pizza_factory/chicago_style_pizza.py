from pizza_abstract_class import PizzaAbstractClass


class ChicagoStyleCheesePizza(PizzaAbstractClass):
    def __init__(self):
        self.name = "Chicago style deep dish cheese pizza"
        self.dough = "Extra thick crust dough"
        self.sauce = "Plum tomato sauce"
        self.toppings.append("Shredded mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")
