from abc import ABC, abstractmethod


class BeverageAbstractClass(ABC):
    description: str = "Unknown beverage"

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass
