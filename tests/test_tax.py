import sys
from unittest import TestCase
sys.path.append('src')
from utils.product import Product


class VatTest(TestCase):
    def test_vat_imported_standar(self):
        vat = Product(category='ciao', is_imported=False,
                      price=5, product_name='pills', quantity=1)
        self.assertTrue(vat.iva == 10)
        self.assertEqual(vat.get_price_tot(), 5 + (5*10)/100)
        self.assertEqual(vat.get_iva_price(), 0.50)

    def test_vat_not_imported(self):
        vat = Product(category='book', is_imported=False, price=5,
                      product_name='harry potter', quantity=1)
        self.assertTrue(vat.iva == 0)
        self.assertEqual(vat.get_price_tot(), 5)
        self.assertEqual(vat.get_iva_price(), 0)

    def test_vat(self):
        vat = Product(category='book', is_imported=True, price=5,
                      product_name='harry potter', quantity=1)
        self.assertTrue(vat.iva == 5)
        self.assertEqual(vat.get_price_tot(), 5 + (5*5)/100)
        self.assertEqual(vat.get_iva_price(), 0.25)

    def test_vat_fail(self):
        vat = Product(category='book', is_imported=True, price=5,
                      product_name='harry potter', quantity=1)
        self.assertTrue(vat.iva != 0)

    def test_product_str(self):
        vat = Product(category='book', is_imported=False, price=5,
                      product_name='harry potter', quantity=1)
        self.assertTrue(vat.__str__() == '1 harry potter at 5.0')

    def test_product_imported_str(self):
        vat = Product(category='book', is_imported=True, price=5,
                      product_name='harry potter', quantity=1)
        self.assertTrue(vat.__str__() == '1 imported harry potter at 5.25')
