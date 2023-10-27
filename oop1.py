class Person:
    def __init__(self,atribute1_name,atribute2_last_name,atribute3_age):
        #instance variable
        print('init method get called')
        self.atribute1_name = atribute1_name
        self.atribute2_last_name = atribute2_last_name
        self.atribute3_age = atribute3_age

p1 = Person('tohidul','islam',25)
p2 = Person('emil','ahmed',24)
print(p1.atribute1_name)
print(p2.atribute1_name)