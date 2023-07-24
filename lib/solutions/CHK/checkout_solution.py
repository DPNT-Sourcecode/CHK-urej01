import math
from item import Item
price_list = {
    'A': Item('A', 50, {5: 200, 3: 130}),
    'B': Item('A', 30, {2: 45}),
    'C': Item('C', 20),
    'D': Item('D', 15,),
    'E': Item('E', 40,  ex_deals={2: 'B'})
}


# def handle_multiples(count, divisor, multiby_price, sku):
#     return math.floor(count/divisor) * multiby_price + \
#             (count % divisor * price_list[sku].cost)
#
#
# def multiby_prices(sku, count):
#     if sku == 'A' and count >= 5:
#         return handle_multiples(count, 5, 200, sku)
#     if sku == 'A' and count >= 3:
#         return handle_multiples(count, 3, 130, sku)
#     if sku == 'B' and count >= 2:
#         return handle_multiples(count, 2, 45, sku)
#     else:
#         return None


def get_discounts(sku, count, skus):
    if sku == 'E' and count >= 2 and skus.find('B') != -1:
        return -30
    else:
        return 0


def get_value(sku, skus):
    count = skus.count(sku)
    discount = get_discounts(sku, count, skus)
    multiples_price = price_list[sku].get_deals(count)
    print(multiples_price)
    return (price_list[sku].cost * count if multiples_price is None else multiples_price) + discount


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

print(checkout("AAA"))




