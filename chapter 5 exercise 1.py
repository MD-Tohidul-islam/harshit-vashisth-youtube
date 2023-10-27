m=map(int,list(input('enter a list with comma sepated: ').split(',')))
def squar(l):
    squar_list = []
    for i in l:
        squar_list.append(i**2)
    return squar_list


#number_list = list(m)
#new = map(int,number_list) 
print(squar(m))
def s(l):
    return [i**2 for i in l ]
v=map(int,list(input('enter a list with comma sepated: ').split(',')))
print(s(v))
