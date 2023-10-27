name = input('enter your name: ')
v=''
for i in range(len(name)):
    if name[i] not in v:
        print(f'{name[i]} is: {name.count(name[i])}')
    v+=name[i]
print('[[[[[[[[[[]]]]]]]]]]]')
str =''
for i in name:
    if i not in str:
        print(f'{i} is : {name.count(i)}')
    str+=i
print()
tem = ''
i = 0
while i<len(name):
    if name[i] not in tem:
        tem+=name[i]
        print(f'{name[i]} : {name.count(name[i])}')
    i+=1