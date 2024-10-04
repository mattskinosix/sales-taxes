import re


def extract_number(string) -> int:
    number = re.findall(r'(\d+) .', string).pop(0)
    return int(number)


def extract_imported(string) -> bool:
    try:
        extraced = re.findall(r'imported', string).pop(0)
        return extraced == 'imported'
    except IndexError:
        return False


def extract_product_name(string) -> str:
    extraced = re.findall(r'(\d+\s+imported)? (.*?) at', string)[0][1]
    return extraced


def extract_price(string) -> float:
    number = re.findall(r'at (\d+\.\d+)', string).pop(0)
    return float(number)
