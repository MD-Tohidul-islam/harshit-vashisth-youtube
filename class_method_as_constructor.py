class person:
    count = 0
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name= last_name
        self.age = age
        person.count += 1
    @classmethod
    def from_string(cls,string):
        first,last,age= string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instance(cls):
        return f'you have created {cls.count} of person class'
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18

p1 = person('tohidul','islam',25)
p2 = person('emil','ahmed',24)
print(p1.full_name())