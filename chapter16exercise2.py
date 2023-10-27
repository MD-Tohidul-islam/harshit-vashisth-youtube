class Laptop:
    def __init__(self,brand,model,name,price):
        self.brand = brand
        self.model = model
        self.name = name
        self.price = price

    def apply_discount(self,discount):
        discount_amount = self.price*(discount/100)
        new_price = self.price-discount_amount
        return new_price

laptop1 = Laptop('hp','au114tx','tohidul',63000)
print(laptop1.apply_discount(5))