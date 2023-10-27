class Laptop:
    discount = 10
    def __init__(self,brand,model,name,price):
        self.brand = brand
        self.model = model
        self.name = name
        self.price = price

    def apply_discount(self):
        discount_amount = self.price*(self.discount/100)
        new_price = self.price-discount_amount
        return new_price

laptop1 = Laptop('hp','au114tx','tohidul',63000)
print(laptop1.apply_discount())
laptop2 = Laptop('apple','notebook','ik12',63000)
laptop2.discount = 50
print(laptop2.apply_discount())
