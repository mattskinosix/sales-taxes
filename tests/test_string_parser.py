import sys
from unittest.case import TestCase
sys.path.append('src')
from utils.string_parser import extract_price, extract_number, extract_imported, extract_product_name


class TestStringParser(TestCase):

    def test_extract_number(self):
        string = "1 imported box of chocolates at 10.00"
        extracted = extract_number(string)
        self.assertEqual(extracted, 1)

    def test_extract_number_fail(self):
        string = "imported box of chocolates at 10.00"
        self.assertRaises(IndexError, extract_number, string)

    def test_imported(self):
        string = "1 imported box of chocolates at 10.00"
        extracted = extract_imported(string)
        self.assertEqual(extracted, True)

    def test_imported_false(self):
        string = "box of chocolates at 10.00"
        extracted = extract_imported(string)
        self.assertEqual(extracted, False)

    def test_price(self):
        string = "1 price box of chocolates at 10.00"
        extracted = extract_price(string)
        self.assertEqual(extracted, 10.00)

    def test_price_fail(self):
        string = "box of chocolates at"
        self.assertRaises(IndexError, extract_price, string)

    def test_product_name(self):
        string = "1 imported box of chocolates at 10.00"
        extracted = extract_product_name(string)
        self.assertEqual(extracted, 'box of chocolates')

    def test_product_name_fail(self):
        string = "1 imported box of chocolates at 10.00"
        self.assertRaises(IndexError, extract_product_name, string)
