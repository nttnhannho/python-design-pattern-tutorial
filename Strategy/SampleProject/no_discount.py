from promote_strategy import PromoteStrategy


class NoDiscountStrategy(PromoteStrategy):
    def do_discount(self, price):
        return price
