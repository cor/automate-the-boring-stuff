import random

name = ''

while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')


for i in range(5):
    print(i)

total = 0
for num in range(101):
    total += num
print(total)

for i in range(12, 16):
    print(i)

for i in range (0, 10, 2):
    print(i)

for i in range (5, -1, -1):
    print(i * random.randit(1, 10))