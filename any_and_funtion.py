n = [1,2,3,4,5,6,7]
n2 = [2,4,6,8,10]
v = all([i%2==0 for i in n2])
print(v)
v1 = all([i%2==0 for i in n2])
print(v1)
v3 = any(i%2==0 for i in n)
print(v3)