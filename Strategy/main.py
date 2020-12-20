from abc import ABC, abstractmethod


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def do_something(self):
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        res = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e'])
        print(''.join(res))


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))


if __name__ == '__main__':
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_something()
    print()
    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_something()
