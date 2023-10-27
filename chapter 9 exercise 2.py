def find_nums(l):
    list1 = []
    for i in l:
        if type(i) ==int or type(i)==float:
            list1.append(str(i))
    li = [str(i) for i in l if type(i)==int or type(i)==float]
    print(li)
    return list1



v = [1,2,3,[3,6,7,7],39,4.5,59.6,[8.7,6,5.6]]
print(find_nums(v))