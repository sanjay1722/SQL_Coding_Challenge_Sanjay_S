'''1. Accept 3 integers from the User and Display Maximum'''

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))

if num1 > num2 and num1 > num3:
  print(num1, 'is the Maximum')
elif num2 > num1 and num2 > num3:
  print(num2, 'is the Maximum')
else:
  print(num3, 'is the Maximum')

