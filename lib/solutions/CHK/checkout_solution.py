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


def count_instances(skus, values_list):

    costs = [get_value(value, skus.count(value)) for value in values_list]
    print(costs)
    print(sum(costs))
    return sum(costs)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if len(skus) < 1 or not skus.isalpha():
        return -1

    count_instances(skus, price_list.keys())




checkout('AAAAAABBBCCD')




