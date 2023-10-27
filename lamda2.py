def func(s):
    if len(s)>5:
        return True
    return False


func2 = lambda s: True if len(s) > 5 else False
print(func2('abds'))