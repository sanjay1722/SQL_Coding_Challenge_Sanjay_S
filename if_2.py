'''2. Accept 3 integers from the User and Display Minimum'''

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))

if num1 < num2 and num1 < num3:
  print(num1, 'is the Minimum')
elif num2 < num1 and num2 < num3:
  print(num2, 'is the Minimum')
else:
  print(num3, 'is the Minimum')