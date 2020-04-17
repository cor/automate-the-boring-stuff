import random
import time
import copy

WIDTH = 200
HEIGHT = 20
INTERVAL = 0.1

next_cells = []

# Initialize the world with random cells
for x in range(WIDTH):
    column = []  # Create a new column
    for y in range(HEIGHT):
        if bool(random.getrandbits(1)):
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)


while True:  # Main program loop.
    print('\n\n\n\n\n')  # Separate each step with newlines.
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')  # Print the # or space.
        print()                                 # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            left_coord   = (x - 1) % WIDTH
            right_coord  = (x + 1) % WIDTH
            top_coord    = (y - 1) % HEIGHT
            bottom_coord = (y + 1) % HEIGHT

            neighbor_coords = ((left_coord, top_coord), (x, top_coord), (right_coord, top_coord),           # top row
                               (left_coord, y), (right_coord, y),                                           # middle row
                               (left_coord, bottom_coord), (x, bottom_coord), (right_coord, bottom_coord))  # bottom row

            # Count number of living neighbors:
            neighbor_count = 0
            for coord in neighbor_coords:
                if current_cells[coord[0]][coord[1]] == '#':
                    neighbor_count += 1

            # Set cell based on Conway's Game of Life rules:
            if current_cells[x][y] == '#' and (neighbor_count == 2 or neighbor_count == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and neighbor_count == 3:
                # Dead cells with 3 neighbors become alive:
                next_cells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                next_cells[x][y] = ' '

    time.sleep(INTERVAL)  # Add a 1-second pause to reduce flickering.

