from abc import ABC, abstractmethod
from beverage_abstract_class import BeverageAbstractClass


class CondimentDecorator(BeverageAbstractClass):

    @abstractmethod
    def get_description(self):
        pass
