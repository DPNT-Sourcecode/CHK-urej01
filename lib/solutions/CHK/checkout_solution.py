def count_instances(skus, values_list):
    print(values_list)
    for value in values_list:
        print(value)
        print(skus.count(value))
        # return skus.count(value)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    allow_list = ['A', 'B', 'C', 'D']

    if len(skus) < 1 or not skus.isalpha():
        return -1

    count_instances(skus, allow_list)

checkout('AAABBBCDE')






