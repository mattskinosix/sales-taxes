from decimal import Decimal
import math


def round_nearest(num: float, to: float) -> float:
    num, to = Decimal(str(num)), Decimal(str(to))
    return float(math.ceil(num / to) * to)
