
class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f'Order({self.order_id}, {self.product}, {self.quantity})'
