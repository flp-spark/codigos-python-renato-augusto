from order import Order

order_1 = Order(amount=200.00)
order_1.apply_fixed_discount(discount=50.00)
print(order_1.get_amount())

order_2 = Order(amount=200.00)
order_2.apply_percentage_discount(percentage=10)
print(order_2.get_amount())