import sys
from unittest import TestCase
import unittest
sys.path.append('src')
from utils.product import Product


class VatTest(TestCase):
    def test_vat_not_imported(self):
        vat = Product(category='book', is_imported=False, price=5)
        self.assertTrue(vat.iva == 0)

    def test_vat(self):
        vat = Product(category='book', is_imported=True, price=5)
        self.assertTrue(vat.iva == 0.25)

    def test_vat_fail(self):
        vat = Product(category='book', is_imported=True, price=5)
        self.assertTrue(vat.iva == 0.35)


if __name__ == '__main__':
    unittest.main()
