from pprint import pprint

board_a = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
board_b = {'1h': 'bking', '2h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
board_c = {'6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
board_d = {'6c': 'wqueen', '6x': 'wbking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}


def is_valid_chess_board(board):
    pieces = list(board.values())
    spaces = list(board.keys())

    # Piece validation
    pieces_are_valid = {'bpawn', 'bbishop', 'brook', 'bqueen', 'bking',
                        'wpawn', 'wbishop', 'wrook', 'wqueen', 'wking'}.issuperset(pieces)

    knights_present = pieces.count('bking') == 1 and \
                      pieces.count('wking') == 1

    piece_count = [p[0] for p in pieces].count('b') <= 16 and \
                  [p[0] for p in pieces].count('w') <= 16

    pawn_count = pieces.count('bpawn') <= 8 and \
                 pieces.count('wpawn') <= 8

    # Space validation
    def is_valid_space(s):
        return int(s[0]) in range(8) and 'a' <= s[1] <= 'h'

    spaces_are_valid = all(is_valid_space(s) for s in spaces)

    return pieces_are_valid and knights_present and piece_count and pawn_count and spaces_are_valid


print(is_valid_chess_board(board_a))
print(is_valid_chess_board(board_b))
print(is_valid_chess_board(board_c))
print(is_valid_chess_board(board_d))
