def count_list(l):
    list1 = 0
    for i in l:
        if type(i) == list:
            list1+=1
    return list1

v= [1,2,3,[45,4],[4,3,2],34,[6,5]]
print(count_list(v))