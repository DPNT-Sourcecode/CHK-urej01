import math


class Item:

    name = ""
    cost = 0
    deals = []

    def __init__(self, name, cost, deals=None, ex_deals=None):
        self.name = name
        self.cost = cost
        self.self_deals = deals
        self.external_deals = ex_deals
        self.has_external_discount = False

    def get_deals(self, item_count):
        costs = []

        if self.self_deals:

            if len(self.self_deals.keys()) > 1 and item_count >= sum(self.self_deals.keys()):
                # do combo price
                max_divisor = max(self.self_deals.keys())
                min_divisor = min(self.self_deals.keys())

                base_price = math.floor(item_count / max_divisor) * self.self_deals[max_divisor]

                remainder_count = item_count % max_divisor
                remainder_price = math.floor(remainder_count / min_divisor) * self.self_deals[min_divisor]

                leftover_count = (remainder_count % min_divisor) * self.cost

                costs.append(base_price + remainder_price + leftover_count)

            for divisor, multiby_price in self.self_deals.items():
                costs.append(math.floor(item_count / divisor) * multiby_price + (item_count % divisor * self.cost))

            return min(costs)
        else:
            return None

    def get_external_deals(self, item_count, discount_cost, full_cost):
        # # ex_deals = {2: 'B'} key is number of items B is the item you get free
        costs = []

        if self.external_deals:
            for divisor, item in self.external_deals.items():
                total_discount = 0
                if discount_cost is not None:
                    total_discount = discount_cost
                if math.floor(item_count / divisor) <= 1:
                    # Do this when divisor is a multiple of 2
                    total_discount = math.floor(item_count / divisor) * full_cost
                costs.append(total_discount)
                self.has_external_discount = True
            return -min(costs)

        else:
            return 0


price_list = {
    'A': Item('A', 50, deals={5: 200, 3: 130}),
    'E': Item('E', 40,  ex_deals={2: 'B'}),
    'B': Item('B', 30, deals={2: 45}),
    'C': Item('C', 20),
    'D': Item('D', 15,),
}


def get_discounts(sku, count, skus):
    if sku == 'E' and count >= 2 and skus.find('B') != -1:
        return price_list[sku].get_external_deals(count,
                                                  skus.count('B'),
                                                  price_list['B'].cost
        )
    else:
        return 0


def get_value(sku, skus):
    count = skus.count(sku)
    if sku == 'B' and price_list['E'].has_external_discount:
        multiples_price = None
    else:
        multiples_price = price_list[sku].get_deals(count)
    discount = get_discounts(sku, count, skus)
    print(f'sku {sku}')
    print(f'multiples_price {multiples_price}')
    print(f'discount {discount}')
    print(f'total price {price_list[sku].cost * count}')
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

print(checkout('CCADDEEBBA')) # 280
print(checkout('EEEEBB')) # 160



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



