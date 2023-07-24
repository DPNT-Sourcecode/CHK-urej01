class Item:

    name = ""
    cost = 0
    deals = []

    def __init__(self, name, cost, deals=None, ex_deals=None):
        self.name = name
        self.cost = cost
        self.self_deals = deals
        self.external_deals = ex_deals

    def get_price(self):
        return cost

    def get_deals(self, item_count):
        costs = []
        print(self.self_deals)
        if self.self_deals:
            for divisor, multiby_price in self.self_deals:
                print(divisor)
                print(multiby_price)
                costs.add(math.floor(item_count / divisor) * multiby_price + (item_count % divisor * self.cost))

            return min(costs)
        else:
            return None






