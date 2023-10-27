# number guessing game
win_number = 55
guess = int(input('guess a number: '))
if guess == win_number:
    print('you win!!!!')
else:
    if guess < win_number:
        print('too low')
    else:
        print('too high')
#using random module
import random
win_number1 =random.randint(1,100)
guess1 = int(input('guess a number: '))
if guess1 == win_number1:
    print('you win!!!!')
elif guess1 < win_number1:
    print('too low')
else:
    print('too high')
#using while loop
i=0
while i<3:
    win_number = 55
    guess = int(input('guess a number: '))
    if guess == win_number:
        print('you win!!!!')
        break
    elif guess < win_number:
        print('too low')
    else:
        print('too high')
    i+=1
j=0
while j<3:
    import random
    win_number1 = random.randint(1, 10)
    guess1 = int(input('guess a number between 1 to 10: '))
    if guess1 == win_number1:
        print('you win!!!!')
    elif guess1 < win_number1:
        print('too low')
    else:
        print('too high')
    j+=1
