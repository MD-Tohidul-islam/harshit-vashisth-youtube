class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price


    def make_a_call(self,phone_number):
        print(f'calling{phone_number}')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        #two way
        #Phone.__init__(self,brand,model_name,price) uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone = Phone('Nokia','1100',1000)
smartphine = Smartphone('oneplus','s',10000,'4 GB','64 GB','20Mp')
print(phone.full_name())
print(smartphine.full_name(),f'and price is: {smartphine._price}')