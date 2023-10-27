def to_power(n):
    def num(x):
        return x**n
    return num

sq = to_power(2)
print(sq(4))
cube = to_power(3)
print(cube(2))