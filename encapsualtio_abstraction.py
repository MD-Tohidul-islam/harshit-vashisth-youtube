class Phone:
    def __init__(self,brand,model_name,price,price1):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        self.__price1 = price1

    def make_a_call(self,phone_number):
        print(f'calling{phone_number}')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def send_massage(self):
        pass
#_name = convention of private name
#__name__= dunder/magic methods
phone1 = Phone('nokia',1110,10000,'price1:20000')
print(phone1._price)
phone1._price = 1200
print(phone1._price)
#print(phone1.__price1)
#print atrribute our class
print(phone1.__dict__)
print(phone1._Phone__price1)


