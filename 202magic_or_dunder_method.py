class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
    def phone_name(self):
        return f'{self.brand} {self.model_name}'
    #str,repr
    def __repr__(self):
        return f'{self.brand} {self.model_name}'
    # we also use can str
    def __str__(self):
        return f'{self.brand} {self.model_name} {self.price}'

my_phone = Phone('Nokia','1100',1000)
print(my_phone)
print(str(my_phone))
print(repr(my_phone))