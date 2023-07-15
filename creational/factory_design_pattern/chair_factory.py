import abc
from factory_concept import InvalidInput


class AbstractChair(abc.ABC):
    @abc.abstractmethod
    def get_dimensions(self):
        pass


class SmallChair(AbstractChair):
    def __init__(self):
        self.width = 40
        self.length = 40
        self.height = 40

    def get_dimensions(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height
        }


class MediumChair(AbstractChair):
    def __init__(self):
        self.width = 50
        self.length = 50
        self.height = 50

    def get_dimensions(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height
        }


class BigChair(AbstractChair):
    def __init__(self):
        self.width = 60
        self.length = 60
        self.height = 60

    def get_dimensions(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height
        }


class ChairFactory:

    @staticmethod
    def get_chair(chair):
        if chair == "small":
            return SmallChair()
        if chair == "medium":
            return MediumChair()
        if chair == "big":
            return BigChair()

        raise InvalidInput(f"Currently we do not manufacture chair of type {chair}")


# client/driver code
if __name__ == "__main__":
    chair = ChairFactory.get_chair("big")
    print(chair.get_dimensions())
