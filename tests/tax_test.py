import sys
from unittest import TestCase
import unittest
sys.path.append('src')
from lib.iva import Iva


class VatTest(TestCase):
    def test_vat_not_imported(self):
        vat = Iva(category='book', is_imported=False, price=5)
        self.assertTrue(vat.iva == 0)

    def test_vat(self):
        vat = Iva(category='book', is_imported=True, price=5)
        self.assertTrue(vat.iva == 0.25)

    def test_vat_fail(self):
        vat = Iva(category='book', is_imported=True, price=5)
        self.assertTrue(vat.iva == 0.35)


if __name__ == '__main__':
    unittest.main()
