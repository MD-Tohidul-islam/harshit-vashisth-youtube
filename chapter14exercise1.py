import time
from functools import wraps
def calculation_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f'Executing ....{function.__name__}')
        t1 = time.time()
        return_value =function(*args,**kwargs)
        t2 = time.time()
        t = t2-t1
        print(f'this function takes {t} second')
        return return_value
    return wrapper

@calculation_time
def  square_finder(n):
    return [i**2 for i in range(1,n+1)]
square_finder(1000000)