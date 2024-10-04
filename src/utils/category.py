from typing import List
from lib.constants import BOOK_KEYWORD, FOOD_KEYWORD, MEDICAL_KEYWORD


def product_name_contains(array: List[str], product_name: str):
    for value in array:
        if value in product_name:
            return True
    return False


def get_category_by_name(product_name: str):
    category = 'standard'
    if product_name_contains(MEDICAL_KEYWORD, product_name):
        category = 'medical'
    elif product_name_contains(FOOD_KEYWORD, product_name):
        category = 'food'
    elif product_name_contains(BOOK_KEYWORD, product_name):
        category = 'book'

    return category
