import abc


class InvalidInput(Exception):
    pass


class AbstractProduct(abc.ABC):
    @abc.abstractmethod
    def create_object(self):
        """An abstract interface method"""


class ConcreteProductA(AbstractProduct):

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self


class ConcreteProductB(AbstractProduct):

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self


class ConcreteProductC(AbstractProduct):

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self


class Factory:
    """Factory Class for concrete classes ConcreteProductA, ConcreteProductB, ConcreteProductC"""
    def create_some_object(self, some_property):
        if some_property == "a":
            return ConcreteProductA()
        if some_property == "b":
            return ConcreteProductB()
        if some_property == "c":
            return ConcreteProductC()
        raise InvalidInput(f"WE currently do not support product type {some_property}")


# client/driver code
if __name__ == "__main__":
    product = Factory().create_some_object("X")
    print(product.name)
