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

    def get_deals(self, item_count):
        costs = []

        if self.self_deals:

            if len(self.self_deals.keys()) > 1 and item_count >= sum(self.self_deals.keys()):
                # do combo price
                max_divisor = max(self.self_deals.keys())
                min_divisor = min(self.self_deals.keys())

                base_price = math.floor(item_count / max_divisor) * self.self_deals[max_divisor]
                # print(f'base price {base_price}')

                remainder_count = item_count % max_divisor
                remainder_price = math.floor(remainder_count / min_divisor) * self.self_deals[min_divisor]
                # print(f' remainder_count {remainder_count}')
                # print(f' min_divisor {min_divisor}')
                # print(f' self.self_deals[min_divisor] {self.self_deals[min_divisor]}')
                # print(f' remainder_price {remainder_price}')

                leftover_count = (remainder_count % min_divisor) * self.cost
                # print(f' leftover_count {leftover_count}')

                costs.append(base_price + remainder_price + leftover_count)

            for divisor, multiby_price in self.self_deals.items():
                costs.append(math.floor(item_count / divisor) * multiby_price + (item_count % divisor * self.cost))
            return min(costs)
        else:
            return None

    def get_external_deals(self, item_count, discount_cost):

        # ex_deals = {2: 'B'} key is number of items B is the item you get free
        costs = []
        if self.external_deals:
            for divisor, item in self.external_deals.items():
                costs.append(discount_cost if discount_cost is not None else math.floor(item_count / divisor) * discount_cost)
            return -min(costs)

        else:
            return 0





