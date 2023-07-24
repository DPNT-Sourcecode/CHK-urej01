import math
price_list = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}

def handle_multiples(count, divisor, multiby_price, sku):
    return math.floor(count/divisor) * multiby_price + \
            (count % divisor * price_list[sku])


def validate_count(sku, count, skus):
    if sku == 'A' and count >= 5:
        return handle_multiples(count, 5, 200, sku)
    if sku == 'A' and count >= 3:
        return handle_multiples(count, 3, 130, sku)
    if sku == 'B' and count >= 2:
        return handle_multiples(count, 2, 45, sku)
    if sku == 'E' and count >= 2 and skus.find('E') != -1:
        return -30
    else:
        return None


def get_value(sku, skus):
    count = skus.count(sku)
    multiples_price = validate_count(sku, count, skus)
    return price_list[sku] * count if multiples_price is None else multiples_price


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


print(checkout('EE'))

# Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+