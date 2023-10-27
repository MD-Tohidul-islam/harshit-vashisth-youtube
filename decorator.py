def decorator_function(any_function):
    def wrapper_func():
        print('this is awesome function')
        func()
    return wrapper_func
def func():
    print('hi how are you?')

var = decorator_function(func)
var()