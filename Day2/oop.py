class Item:
    pay_rate = 0.8 # the rate of pay after 20% discount
    def __init__(self, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self objects
        name = input("What is your name? ")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        price = self.price * self.pay_rate
        return price * self.quantity

item1 = Item(100, 5)
print(item1.calculate_price())
print(item1.__dict__)
