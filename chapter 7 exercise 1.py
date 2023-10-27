def cube_finder(n):
    cube = {}
    for i in range(len(n)):
        cube[n[i]]=n[i]**3
    return cube

b = [9,2,3,4,5,8]
print(cube_finder(b))
def cubefinder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i]= i**3
    return cube
print(cubefinder(10))