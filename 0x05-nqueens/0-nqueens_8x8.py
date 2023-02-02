#!/usr/bin/python3
"""
contains n queens solution implementation

-> for 8 x 8 chess board
"""

import pprint

def place_piece(board, total_n, placed_pieces, tmp_row=0, tmp_col=0):
    '''attempts to place queen on board

    Args:
        board - chess board
        total_n - number of pieces to arrange
        placed_pieces - total number of pieces placed
        row - row to start at
        col - column to start at

    O = not checked
    X = checked
    Q = occupied by queen

    Time: O(n^4)
    Space: O(n^2)
    '''

    for row in range(tmp_row, 8):
        for col in range(tmp_col, 8):
            if board[row][col] == 'O':
                board[row][col] = 'Q'
                placed_pieces += 1
                if placed_pieces == total_n:
                    return True
                # mark squares checked by current piece
                mark_checked_by_piece(row, col, board)
                return place_piece(board, total_n, placed_pieces, 0, 0)
    return False

def mark_checked_by_piece(row, col, board):
    '''finds rows that are blocked by piece at given position
    
    Args:
        row: row occupied by piece
        col: column occupied by piece
    Returns:
        list of lists of row, col pairs representing occupied spaces
    '''
    # west
    tmp_row = row
    tmp_col = col - 1
    while tmp_col >= 0:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_col -= 1

     # north west
    tmp_col = col - 1
    tmp_row = row - 1
    while tmp_col >= 0 and tmp_row >= 0:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_col -= 1
        tmp_row -= 1

    # north
    tmp_col = col
    tmp_row = row - 1
    while tmp_row >= 0:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_row -= 1

    # north east
    tmp_row = row - 1
    tmp_col = col + 1
    while tmp_col < 8 and tmp_row >= 0:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_row -= 1
        tmp_col += 1

    # east
    tmp_col = col + 1
    tmp_row = row
    while tmp_col < 8:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_col += 1

    # south east
    tmp_row = row + 1
    tmp_col = col + 1
    while tmp_col < 8 and tmp_row < 8:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_row += 1
        tmp_col += 1

    # south
    tmp_row = row + 1
    tmp_col = col
    while tmp_row < 8:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_row += 1

    # south west
    tmp_col = col - 1
    tmp_row = row + 1
    while tmp_row < 8 and tmp_col >= 0:
        if board[tmp_row][tmp_col] != 'Q':
            board[tmp_row][tmp_col] = 'X'
        tmp_col -= 1
        tmp_row += 1



n = 4

def board():
    '''Creates new chess board'''
    chess_board = []
    for _ in range(8):
        chess_board.append(['O']*8)
    return chess_board

def n_queens(n):
    board_solns = []
    for row in range(9):
        for col in range(9):
            chess_board = board()
            if place_piece(chess_board, n, 0, row, col):
                board_solns.append(chess_board)
    return board_solns

def get_queen_positions(board, n):
    '''Fetches the positions occupied by queen pieces
    
    Args:
        board: the chess board
        n: number of queens to fetch
    Return:
        A list of positions occupied by queen pieces
    '''
    if board is None:
        return []
    positions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'Q':
                positions.append([row, col])
                if len(positions) == n:
                    break
        if len(positions) == n:
            break
    return positions

print()
filled_boards = n_queens(6)
for filled_board in filled_boards:
    print(get_queen_positions(filled_board, 6))
    # pprint.pprint(filled_board)
