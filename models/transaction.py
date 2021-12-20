class Transaction:
    def __init__(self, name, price, merchant, tag, timestamp):
        self.name = name
        self.price = price
        self.merchant = merchant
        self.tag = tag
        self.timestamp = timestamp