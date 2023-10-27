def divie(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("you can not a number by zero")
    except TypeError as err:
        print(err,'number must be int or float')
    except :
        print('unexepter error')

print(divie(10,0))
