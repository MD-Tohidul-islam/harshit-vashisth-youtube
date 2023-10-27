def even_odd_list(l):
    even_odd = [[],[]]
    even= []
    odd = []
    for i in l:
        if i%2==0:
            even_odd[0].append(i)
            even.append(i)
        else:
            even_odd[1].append(i)
            odd.append(i)
    out = [even , odd ]
    return even_odd ,out

v=list(range(1,20))
print(even_odd_list(v))