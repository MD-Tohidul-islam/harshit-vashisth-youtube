def sq(a):
    return a**2
l =[1,2,3,4,5,6,7,8,9,12,3,4,56,7,8,9,45,6,789,23]
square = list(map(sq,l))
print(square)
square2 = list(map(lambda a: a**2,l))
print(square2)

# without list coprehension or map function
new_list = []
for num in l:
    new_list.append(sq(num))

print(new_list)
names = ['abc','abcs','abcde','tohidul']
length1 = list(map(len,names))
for i in length1:
    print(i)
print('............')
for j in length1:
    print(j)
print(',,,,,,,,,,,,,,,,')
length = map(len,names)
for i in length:
    print(i)
print('............')
for j in length:
    print(j)