def get_value(sku, count):


def count_instances(skus, values_list):
    print(values_list)
    for value in values_list:
        get_value(value, skus.count(value))
        # return skus.count(value)

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    allow_list = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    if len(skus) < 1 or not skus.isalpha():
        return -1

    count_instances(skus, allow_list.keys())

checkout('AAABBBCDE')







