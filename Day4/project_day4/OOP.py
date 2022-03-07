
# A class to create the product
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >=0
        assert quantity >= 0
        
        # assign self objects
        self.name = name
        self.price = price
        self.quantity = quantity
        


    def calculate_total(self):
        return self.price * self.quantity



item1 = Item("Phone", 100, 5)
print(item1.calculate_total())

