# The Strategy pattern suggests that you take a class that does something specific in a lot of different ways and
# extract all of these algorithms into separate classes called strategies.

# The original class, called context, must have a field for storing a reference to one of the strategies.
# The context delegates the work to a linked strategy object instead of executing it on its own.

# The context isn’t responsible for selecting an appropriate algorithm for the job. Instead, the client passes the
# desired strategy to the context. In fact, the context doesn’t know much about strategies. It works with all
# strategies through the same generic interface, which only exposes a single method for triggering the algorithm
# encapsulated within the selected strategy.

# This way the context becomes independent of concrete strategies, so you can add new algorithms or modify
# existing ones without changing the code of the context or other strategies.

import abc
from typing import List, Union


class Strategy(abc.ABC):
    @abc.abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List):
        print("Normal sorting")
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List):
        print("Reverse sorting")
        return sorted(data, reverse=True)


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def use_case(self, data: Union[List[str], List[int]]) -> List:
        return self._strategy.do_algorithm(data)


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print(context.use_case([9, 5, 4, 0, 4, 8, 0, 0, 8, 7]))

    context = Context(ConcreteStrategyB())
    print(context.use_case(['a', 'e', 'i', 'o', 'u']))
