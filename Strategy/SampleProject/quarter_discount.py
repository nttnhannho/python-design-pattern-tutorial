from promote_strategy import PromoteStrategy


class QuarterDiscount(PromoteStrategy):
    def do_discount(self, price):
        return price * 3/4
