# Single Responsibility Priciple

class Journal:
    def __init__(self):
        # Attributes
        self.entries = []
        self.count = 0

    #Methods of the class
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

class Persistence:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry("It is a good day!")
j.add_entry("Bob came in late!")
print(f'Journal entries:\n{j}')

file = r'U:\journal.txt'
Persistence.save_to_file(j,file)

with open(file) as fh:
    print(fh.read())