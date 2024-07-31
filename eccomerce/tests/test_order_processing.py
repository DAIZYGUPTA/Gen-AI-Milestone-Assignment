
import unittest
from ecommerce.product_management.product import Product
from ecommerce.order_processing.order import Order

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        product = Product(1, 'Sample Product', 19.99)
        order = Order(1001, product, 2)
        self.assertEqual(order.order_id, 1001)
        self.assertEqual(order.product, product)
        self.assertEqual(order.quantity, 2)

if __name__ == '__main__':
    unittest.main()
