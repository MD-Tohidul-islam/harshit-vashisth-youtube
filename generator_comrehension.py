import time
t1 = time.time()
square = (i**2 for i in range(1,1000))
print(square)
print()
for num in square:
    print(num)
print('time for run:',time.time()-t1)
t2=time.time()
l=[i**2 for i in range(1,1000)]
print(l)
print(time.time()-t2)
# in generator we can not print 2nd time.
# after print one time it delete the value from memory
for i in square:
    print(i)