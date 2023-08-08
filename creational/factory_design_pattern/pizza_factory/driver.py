from ny_pizza_store import NYPizzaStore
from chicago_pizza_store import ChicagoStylePizzaStore


def main():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoStylePizzaStore()

    ny_pizza = ny_store.order_pizza(type="cheese")
    print("#####################################")
    chicago_pizza = chicago_store.order_pizza(type="pizza")


if __name__ == "__main__":
    main()
