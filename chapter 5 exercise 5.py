def common(l1,l2):
    out = []
    for i in l1:
        if i in l2:
            out.append(i)
    l1 = set(l1)
    l2 = set(l2)
    common_num = l1 & l2
    return common_num,'and other methode result: ',out
v1 =[1,2,3,4,5,6,7]
v2 =[4,8,9,3,1,90,87]
print(common(v1,v2))

