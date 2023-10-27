def is_even(a):
    return a%2 == 0


numbers = [1,2,3,4,5,6,7,8,9,10]
v = list(filter(is_even,numbers))
print(v)
b = list(filter(lambda a: a%2==0 , numbers))
print(b)
