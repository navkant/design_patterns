import abc


class AbstractProduct(abc.ABC):
    @abc.abstractmethod
    def create_object(self):
        """abstract interface method"""


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


class FactoryA:
    def create_object(self, factory):
        if factory == 'a':
            return ConcreteProductA().create_object()
        if factory == 'b':
            return ConcreteProductB().create_object()
        if factory == 'c':
            return ConcreteProductC().create_object()
