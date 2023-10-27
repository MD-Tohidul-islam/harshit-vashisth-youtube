class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def calc_circumference(self):
        return 2*Circle.pi*self.radius


circle1 = Circle(4)
circle2 =Circle(5)
print(circle1.calc_circumference())
class Laptop:
    discount = 10
    def __init__(self,brand,model,name,price):
        self.brand = brand
        self.model = model
        self.name = name
        self.price = price

    def apply_discount(self):
        discount_amount = self.price*(Laptop.discount/100)
        new_price = self.price-discount_amount
        return new_price

laptop1 = Laptop('hp','au114tx','tohidul',63000)
print(laptop1.apply_discount())