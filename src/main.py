import logging
from typing import List
from utils.category import get_category_by_name
from utils.product import Product
from utils.string_parser import extract_imported, \
    extract_number, \
    extract_price, \
    extract_product_name


basket1 = [
    '1 book at 12.49',
    '1 music CD at 14.99',
    '1 chocolate bar at 0.85'
]

basket2 = [
    '1 imported box of chocolates at 10.00',
    '1 imported bottle of perfume at 47.50'
]

basket3 = [
    '1 imported bottle of perfume at 27.99',
    '1 bottle of perfume at 18.99',
    '1 packet of headache pills at 9.75',
    '1 box of imported chocolates at 11.25',
]


def calculate_receipt(basket: List[str]):
    total = 0
    sale_taxes: float = 0

    for product in basket:
        try:
            price = extract_price(product)
            product_name = extract_product_name(product)
            quantity = extract_number(product)
            imported = extract_imported(product)
            product = Product(
                price=price,
                quantity=quantity,
                is_imported=imported,
                product_name=product_name,
                category=get_category_by_name(product_name)
            )
            print(product)
            total += product.get_price_tot()
            sale_taxes += product.get_iva_price()
        except Exception:
            logging.exception(f"Error processing {product}: ")
            continue
    print('Sales Taxes: %.2f' % sale_taxes)
    print('Total: %.2f' % total)


if __name__ == '__main__':

    basket_to_use = basket1
    number = int(input("Give me basket number to test (default = 1 ): "))
    if number == 1:
        basket_to_use = basket1
    elif number == 2:
        basket_to_use = basket2
    elif number == 3:
        basket_to_use = basket3
    calculate_receipt(basket_to_use)
