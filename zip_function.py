user_id =['user1','user2','user3','user4','user5']
names = ['tohidul','emil','razu','salman']
last_name = ['islam','ahmed','ahmed','khan']
v = list(zip(user_id,names))
print(v)
v1 = list(zip(user_id,names,last_name))
print(v1)
b = [('a',1),('b',2),('c',3)]
print(dict(b))
# as like we can make a dict from zip
print(dict(v))
# we can not make as like as zip to dict