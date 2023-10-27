def func(num,*args):
    v=[]
    for i in args:
        v.append(i**num)
    return v
num = 3
#ar = [1,2,3]
print(func(num,1,2,3))
def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return 'you did not pass any args'
nums=[1,2,3]
print(to_power(3,*nums))
