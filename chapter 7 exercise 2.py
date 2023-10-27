user ={}
name = input('what is your name?: ')
age = input("what is your age?: ")
fav_movies = input('enter your favorite movies separared by comma: ').split(',')
fav_song = input('enter your favorite song separared by comma: ').split(',')


user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_song
for key,values in user.items():
    print(f'{key} : {values}')
