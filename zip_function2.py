l1 = [1,2,3,4,5,10]
l2 = [2,4,6,8,9,3]
l = [(1,2),(3,4),(5,6),(7,9)]

# * operator with zip
# to unpake list(l)
print(list(zip(*l)))
l3,l4 = list(zip(*l))
print(l3)
print(l4)
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)