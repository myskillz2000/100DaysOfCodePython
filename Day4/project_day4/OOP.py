
# A class to create the product
class Item:
    def __init__(self, name):

    def calculate_total(self, x, y):
        return x * y



item1 = Item("Phone")
item1.price = 100
item1.quantity = 5
total = item1.calculate_total(item1.price, item1.quantity)
print(total)
