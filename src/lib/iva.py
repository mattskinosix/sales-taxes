from typing import List
from .constants import IVA


class Iva:
    __exempt_category: List[str] = ['book', 'food', 'medical']

    def __init__(self, category: str, is_imported: bool, price: int):
        iva = 10
        if category in self.__exempt_category:
            iva = 0
        if is_imported:
            iva = round((price * IVA)/100, 2)

        self.iva = iva
