def func(l,**kargs):
    if kargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names = ['tohidul','emil','razu']
print(func(names))
print(func(names,reverse_str=True))