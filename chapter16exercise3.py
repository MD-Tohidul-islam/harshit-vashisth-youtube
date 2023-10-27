class person:
    count = 0
    def __init__(self,name):
        self.name = name
        person.count += 1



    #def count_instance(self):
p1 = person('tohidul')
print(p1.count)
p2 = person('emil')
print(p2.count)
print(p1.count)

