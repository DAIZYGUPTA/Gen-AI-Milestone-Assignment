
import unittest
from ecommerce.product_management.product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product(1, 'Sample Product', 19.99)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, 'Sample Product')
        self.assertEqual(product.price, 19.99)

if __name__ == '__main__':
    unittest.main()
