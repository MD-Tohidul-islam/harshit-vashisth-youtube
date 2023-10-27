name = ['abc','abcd','tohidul','emil']
pos = 0
for i in name:
    print(f'{pos}---------->{i}')
    pos+=1

for pos1 , j in enumerate(name):
    print(f'{pos1}--->{j}')

pos2 = 0
def find_pos(l,target):
    for pos2 , j in enumerate(l):
        if j == target:
            return pos2
    return -1
print(find_pos(name,'tohidul'))
def find_pos2(l,target):
    for i in l:
        if i == target:
            return l.index(i)
    return -1
print(find_pos(name,'tohidul'))