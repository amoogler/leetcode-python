class OrderedStream:

    def __init__(self, n: int):
        self.orders = [''] * n
        self.order_count = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.orders[idKey - 1] = value
        next_orders = []

        for order in self.orders[self.order_count:]:
            if not order:
                return next_orders
            else:
                next_orders.append(order)
                self.order_count += 1

        return next_orders


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)