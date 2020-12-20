from abc import ABC, abstractmethod


class PromoteStrategy(ABC):
    @abstractmethod
    def do_discount(self, price):
        pass
