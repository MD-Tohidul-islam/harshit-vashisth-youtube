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
    def full_name(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'
class Flagshiphone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f'{self.brand} {self.model_name} and price is {self._price} and rear_camera is {self.rear_camera}'
oneplus5 = Smartphone('oneplus','s',10000,'4 GB','64 GB','20Mp')
oneplus5t = Flagshiphone  ('oneplus','s',10000,'4 GB','64 GB','20Mp','16Mp')
# print(smartphine.full_name())
# print(oneplus.full_name())
# print(help(Smartphone))
print(isinstance(oneplus5,Smartphone))
print(isinstance(oneplus5,Phone))
print(isinstance(oneplus5,Flagshiphone))