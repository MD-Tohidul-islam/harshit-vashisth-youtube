# list comprention
square = [i**2 for i in range(1, 11)]
print(square)
even_num = [i for i in range(1,11) if i%2==0]
print(even_num)
#if else
mixed = [j*2 if (j%2==0) else -j for j in range(1,11)]
print(mixed)
n1 = [[i for i in range(1,4)] for j in range(3)]
print(n1)