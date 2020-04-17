import random

spam = [['cat', 'bat'], [10, 20, 30, 42, 50]]
test = ['cat', 'bat', 'rat', 'elephant']


print(spam[-1][3])
print(spam[1][0:2])
print(test[0:-1])
print(test[:2])
print(len(test))

test[1] = 'aardvark'
print(test)

a = [1, 2, 3] + ['A', 'B', 'C'] * 3

print(a)

del a[3]

print(a)

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])


pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))

print(pets)
random.shuffle(pets)
print(pets)

print(['hello', 'hi', 'howdy', 'heyas'].index('hi'))

pets.append('Fox')
pets.insert(1, 'Chicken')

print(pets)

pets.remove('Chicken')
print(pets)

pets.sort(reverse=True)

print(pets)

characters = ['a', 'B', 'z', 'D']
characters.sort(key=str.lower, reverse=True)
print(characters)


for c in 'Breath of the Wild':
    print(f'***<- {c} ->***')

