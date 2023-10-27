def avr(*args):
    avrg = []
    for i in args:
        c = sum(i)/len(i)
        avrg.append(c)
    return avrg
print(avr([1,2,3],[4,5],[6,7,8]))
def average_finder(l1,l2):
    average = []
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average

print(average_finder([1,2,3],[4,5,6]))
def average_finder(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average

print(average_finder([1,2,3],[4,5,6],[7,8,9]))
average2 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(list(average2([1,2,3],[4,5,6],[7,8,9])))