import abc
from abc import ABC


class Subject(ABC):
    @abc.abstractmethod
    def register_observer(self, observer: "Observer"):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer: "Observer"):
        pass


class Observer(ABC):
    @abc.abstractmethod
    def update(self, temp: float, humidity: float, pressure: str):
        pass


class DisplayElement(ABC):
    @abc.abstractmethod
    def display(self):
        pass
