import math
price_list = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}


def handle_multiples(count, divisor, multiby_price, sku):
    return math.floor(count/divisor) * multiby_price + \
            (count % divisor * price_list[sku])


def multiby_prices(sku, count):
    if sku == 'A' and count >= 5:
        return handle_multiples(count, 5, 200, sku)
    if sku == 'A' and count >= 3:
        return handle_multiples(count, 3, 130, sku)
    if sku == 'B' and count >= 2:
        return handle_multiples(count, 2, 45, sku)
    else:
        return None


def get_discounts(sku, count, skus):
    if sku == 'E' and count >= 2 and skus.find('B') != -1:
        return -30
    else:
        return 0


def get_value(sku, skus):
    count = skus.count(sku)
    discount = get_discounts(sku, count, skus)
    multiples_price = multiby_prices(sku, count)
    return (price_list[sku] * count if multiples_price is None else multiples_price) + discount


def get_cost(skus, values_list):
    costs = [get_value(value, skus) for value in values_list]
    return sum(costs)


def validate_value(skus, validate_list):
    return all(sku in validate_list for sku in skus)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not validate_value(skus, price_list.keys()):
        return -1

    return get_cost(skus, price_list.keys())
