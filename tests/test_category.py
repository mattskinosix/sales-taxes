import sys
from unittest.case import TestCase
sys.path.append('src')
from utils.category import get_category_by_name


class TestCategory(TestCase):
    def test_category_standard(self):
        category = get_category_by_name('name')
        self.assertEqual(category, 'standard')

    def test_category_food(self):
        category = get_category_by_name('box of chocolate')
        self.assertEqual(category, 'food')

    def test_category_book(self):
        category = get_category_by_name('book')
        self.assertEqual(category, 'book')

    def test_category_medical(self):
        category = get_category_by_name('pills for head')
        self.assertEqual(category, 'medical')
