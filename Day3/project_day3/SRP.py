import os

# Single Responsibility Principle or Seperation of concerns
class Inventory:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_inventory(self, item):
        self.count +=1
        self.entries.append(f'{self.count}: {item}')

    def remove_inventory(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

class PersistenceManager:
    @staticmethod
    def save_to_file(Inventory, filename):
        file = open(filename, 'w')
        file.write(str(Inventory))
        file.close()

j = Inventory()
j.add_inventory('Iphone')
j.add_inventory('Android')

script_directory = os.getcwd()
file = os.path.join(script_directory, 'Inventory.txt')
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())

