from ticket import Ticket
import no_discount
import quarter_discount
import half_discount


if __name__ == '__main__':
    print('Start getting tickets!')
    ticket = Ticket('ticket1', 200, no_discount.NoDiscountStrategy())
    print(f'ticket1: {ticket.get_promoted_price()}')
    ticket.name = 'ticket2'
    ticket.price = 1000
    ticket.promote_strategy = quarter_discount.QuarterDiscount()
    print(f'ticket2: {ticket.get_promoted_price()}')
    ticket.name = 'ticket3'
    ticket.price = 500
    ticket.promote_strategy = half_discount.HalfDiscount()
    print(f'ticket3: {ticket.get_promoted_price()}')
