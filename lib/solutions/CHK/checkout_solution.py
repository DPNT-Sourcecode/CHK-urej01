import math
price_list = {'A': 50, 'B': 30, 'C': 20, 'D': 15}


def handle_multiples(count, divisor, multiby_price, sku):
    return math.floor(count/divisor) * multiby_price + \
            (count % divisor * price_list[sku])


def validate_count(sku, count):
    if sku == 'A' and count > 3:
        return handle_multiples(count, 3, 130, sku)
    if sku == 'B' and count > 2:
        return handle_multiples(count, 2, 45, sku)
    else:
        return None


def get_value(sku, count):
    multiples_price = validate_count(sku, count)
    return price_list[sku] * count if multiples_price is None else multiples_price


def get_cost(skus, values_list):
    costs = [get_value(value, skus.count(value)) for value in values_list]
    return sum(costs)


def validate_value(skus, validate_list):
    return all(sku in validate_list for sku in skus)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if skus.isalpha():
        return -1
    if not validate_value(skus, price_list.keys()):
        return -1

    return get_cost(skus, price_list.keys())


print(checkout("ABCa"))
