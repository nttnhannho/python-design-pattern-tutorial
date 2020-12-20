class Ticket:
    def __init__(self, name, price, promote_strategy):
        self._name = name
        self._price = price
        self._promote_strategy = promote_strategy

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def promote_strategy(self):
        return self._promote_strategy

    @promote_strategy.setter
    def promote_strategy(self, value):
        self._promote_strategy = value

    def get_promoted_price(self):
        return self._promote_strategy.do_discount(self._price)
