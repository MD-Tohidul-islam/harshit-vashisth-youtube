def reverse_list(l):
    r = []
    a=[]
    for i in range(len(l),0,-1):
        r.append(l[i-1])
    for j  in range(len(l)):
        a.append(l.pop())
    return r ,a


v = [2,34,3,2,4,6,7,8,9]
re = v.reverse()
c = v[::-1]
print(c) 
print(reverse_list(v))