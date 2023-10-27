num1 = int(input('enter 3 numbers:'))
num2 = int(input('enter 3 numbers:'))
num3 = int(input('enter 3 numbers:'))
sum1= num1+num3+num2
average = sum1/3
print(f'average of three numbers is {average}')
n1,n2,n3 = input('enter 3 number with comma separete').split(',')
print(f'average of three numbers is {(int(n1)+int(n2)+int(n3))/3}')
num4 = input('enter 3 number with comma separete').split(',')
num4 = map(int,num4)
print(f'average of 3 numbers is {sum(num4)/3}')


