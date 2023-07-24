allow_list = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

def handle_multiples(count, divisor, multiby_price):
    if count % divisor == 0:
        return (count/divisor) * multiby_price
    else:



def validate_count(sku, count):
    if sku == 'A' and count > 3:
        return handle_multiples(count, 3, 130)
    if sku == 'B' and count > 2:
        return handle_multiples(count, 2, 45)


def get_value(sku, count):
    validate_count(sku, count)
    return allow_list[sku] * count


def count_instances(skus, values_list):
    print(values_list)
    for value in values_list:
        print(get_value(value, skus.count(value)))
        # return skus.count(value)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if len(skus) < 1 or not skus.isalpha():
        return -1

    count_instances(skus, allow_list.keys())

checkout('AAABBBCDE')





