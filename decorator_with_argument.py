from functools import wraps


def only_data_type_allow(data_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            data_types = []
            for arg in args:
                data_types.append(type(arg)==data_type)
            if all(data_types):
                return func(*args,**kwargs)
            else:
                print('ivalid arguments')
        return wrapper
    return decorator
@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string+=i
    return string

print(string_join('tohidul',' islam'))