import random
win_num= random.randint(0,10)
i =0
while True:
    guess = int(input('guess a number: '))
    if guess == win_num:
        print(f'you win!!! and guessed this in {i+1} times')
        break
    else:
        if guess<win_num:
            print('too low!!')
        else:
            print('too high')
    i+=1
