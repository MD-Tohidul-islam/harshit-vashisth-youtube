class Laptop:
    def __init__(self,name,ram,memory,year,price):
        self.name = name
        self.ram = ram
        self.memory = memory
        self.year = year
        self.price = price

laptop1 = Laptop('Hp','4GB','1T',2017,50000)
print(laptop1)
print(laptop1.price)