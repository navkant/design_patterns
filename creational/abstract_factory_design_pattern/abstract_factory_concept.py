import abc
from factory_a import FactoryA
from factory_b import FactoryB


class AbstractAbstractFactory(abc.ABC):
    @abc.abstractmethod
    def create_object(self, factory):
        """abstract factory method"""


class AbstractFactory(AbstractAbstractFactory):
    def create_object(self, factory):
        if factory in ['aa', 'ab', 'ac']:
            return FactoryA().create_object(factory[1])
        if factory in ['ba', 'bb', 'bc']:
            return FactoryB().create_object(factory[1])


if __name__ == "__main__":
    product = AbstractFactory().create_object('bc  ')
    print(product.name)
