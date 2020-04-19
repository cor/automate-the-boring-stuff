grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Simple double for loop implementation.
for y in range(0, len(grid[0])):
    for x in range(0, len(grid)):
        print(grid[x][y], end='')
    print()

print()  # separate the two implementations

# zip-based grid rotation: https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
for x in zip(*grid[::-1]):
    print(''.join(x))
