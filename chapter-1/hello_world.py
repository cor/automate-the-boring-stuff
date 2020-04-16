# Basic 'Hello world' type of program that asks for name and age
print('Hello, world!')

print('What is your name?')
my_name = input()
print(f'It is good to meet you, {my_name} ({len(my_name)})')

print()

print('What is your age?')
my_age = input()
print(f'You will be {str(int(my_age) + 1)} in a year.')

