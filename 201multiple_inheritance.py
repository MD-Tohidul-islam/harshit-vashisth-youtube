class A:
    def class_a_method(self):
        return 'I \'am just a class A method'
    def hello(self):
        return 'hello from class A'

class B:
    def class_b_method(self):
        return "i am just class B method"
    def hello(self):
        return 'hello from class B'

class C(A,B):
    pass
instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())