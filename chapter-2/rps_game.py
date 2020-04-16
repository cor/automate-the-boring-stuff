import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

# The main game loop.
while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    # The player input loop.
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()

        if player_move == 'q':
            sys.exit() # Quit the program.
        if player_move in ('r', 'p', 's'):
            break # Break out of the player input loop.

        # Invalid input
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    computer_input = random.choice((('r', 'ROCK'), ('p', 'PAPER'), ('s', 'SCISSORS')))
    computer_move = computer_input[0]
    print(computer_input[1])

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move, computer_move) in (('r', 's'), ('p', 'r'), ('s', 'p')):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
