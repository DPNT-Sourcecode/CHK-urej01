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
                min_divisor = max(self.self_deals.keys())

                base_price = math.floor(item_count / max_divisor) * self.self_deals[max_divisor]

                remainder_count = item_count % max_divisor
                remainder_price = math.floor(remainder_count / min_divisor) * self.self_deals[min_divisor]

                leftover_count = remainder_count % min_divisor

                costs.append(base_price + remainder_price + leftover_count)

            for divisor, multiby_price in self.self_deals.items():
                costs.append(math.floor(item_count / divisor) * multiby_price + (item_count % divisor * self.cost))
            return min(costs)
        else:
            return None

    def get_external_deals(self, item_count):
        return


