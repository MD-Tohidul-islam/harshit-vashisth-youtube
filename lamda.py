def add(a,b):
    return a+b
add2 = lambda a,b:a+b

def is_even(a):
    if a%2==0:
        return True
    else:
        return False
is_even2 = lambda a : a%2 == 0
def last_char(s):
        return s[-1]
last_char2 = lambda s : s[-1]
print(last_char2('tohidul'))
print(last_char('tohidul'))
print(is_even2(3))
print(add2(3,4))
print(add(3,4))