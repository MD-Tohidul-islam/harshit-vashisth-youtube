from functools import wraps
def print_fuction_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f'you are calling {function.__name__}')
        print(f'{function.__doc__}')
        return function(*args,**kwargs)
    return wrapper

@print_fuction_data
def add(a,b):
    '''this function takes two numbers as arguments and return
their sum'''
    return a+b

print(add(3,4))