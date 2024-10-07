'''1. Accept Integers from User till Users Choice and do the Following:
1. Sum of all Integers
2. Average of all Integers
3. Maximum Integer from all
4. Minimum Integer from all'''

itr = int(input('Enter the number of integers: '))
arr = []
for i in range(itr):
  num = int(input('Enter a number: '))
  arr.append(num)

print('Sum of all Integers={}'.format(sum(arr)))
print('Average of all Integers={}'.format(sum(arr)/itr))
print('Maximum Integer from all={}'.format(max(arr)))
print('Minimum Integer from all={}'.format(min(arr)))