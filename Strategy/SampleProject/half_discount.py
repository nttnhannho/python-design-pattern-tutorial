from promote_strategy import PromoteStrategy


class HalfDiscount(PromoteStrategy):
    def do_discount(self, price):
        return price * 1/2
