from .misc import round_nearest
from .constants import EXEMPT_CATEGORY, IVA_0, IVA_10, IVA_5


class Product:
    iva: float
    price_tot: float
    price_no_iva: float
    iva_price: float
    product_name: str
    is_imported: bool
    category: str

    def __init__(
        self,
        product_name: str,
        is_imported: bool,
        price: float,
        quantity: int,
        category: str
    ):
        iva = IVA_10

        if category in EXEMPT_CATEGORY:
            iva = IVA_0
        if is_imported:
            iva += IVA_5

        self.product_name = product_name
        self.category = category
        self.is_imported = is_imported
        self.iva = iva
        self.price = price
        self.quantity = quantity

    def get_price_tot(self):
        return round(self.price + self.get_iva_price(), 2)

    def get_iva_price(self):
        price = round_nearest(self.price * self.iva / 100, 0.05)
        return price

    def __str__(self) -> str:
        return f"""{self.quantity}{' imported' if self.is_imported else ''} {self.product_name} at {self.get_price_tot()}"""
