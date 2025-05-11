"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(array.count(X) for array in board)
    o_count = sum(array.count(O) for array in board)
    
    if x_count == 0 and o_count == 0:
        return X
    elif x_count > o_count:
        return O
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if board[i][j] != EMPTY:
        raise NameError('not a valid action')
    board_copy = copy.deepcopy(board)
    board_copy[i][j]=player(board)
    return board_copy
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!= EMPTY:
            return row[0]
    for column in range(3):
        if board[0][column]== board[1][column]== board[2][column] and board[0][column]!= EMPTY:
            return board[0][column]
    
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[0][2]==board[1][1]==board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = sum(array.count(EMPTY) for array in board)
    if empty_count == 6:
        return False
    else:
        True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
