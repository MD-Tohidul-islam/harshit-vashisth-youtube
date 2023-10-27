def even_generator(n):
    for num in range(1,n+1):
        if num%2==0:
            yield num

print(even_generator(20))
even_nums = even_generator(20)
print(even_nums)
print(next(even_generator(20)))
print('...................')
for num in even_generator(20):
    print(num)
