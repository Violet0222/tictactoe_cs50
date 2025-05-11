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
    board_copy = copy.deepcopy(board)
    try:
        if board_copy[action[0]][action[1]] != EMPTY:
            raise IndexError
        elif action[0]<0 or action[0]>2 or action[1]<0 or action[1]<2:
            raise IndexError
        else:  
            board_copy[action[0]][action[1]]=player(board)
            return board_copy
    except IndexError:
        print('not a valid action')
    


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
    for row in board:
        if EMPTY in row and winner(board) == None:
            return False
    if winner(board) != None:
        return True  
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board)== True:
        if winner(board)== X:
            return 1
        elif winner(board)== O:
            return -1
        else:
            return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    
    def max_value(board):
        if terminal(board) == True:
             return utility(board)
        max_possible_value=-math.inf
        for action in actions(board):
            max_possible_value=max(max_possible_value, min_value(result(board,action)))
        return max_possible_value
    
    def min_value(board):
        if terminal(board) == True:
             return utility(board)
        minimal_possible_value = math.inf
        for action in actions(board):
            minimal_possible_value=min(minimal_possible_value, max_value(result(board,action)))
        return minimal_possible_value

    
    current_player = player(board)
    
    if current_player == X:
        best_score = -math.inf
        best_action = None
        
        for action in actions(board):
            copy_board = result(board, action)
            opponent_best_score = min_value(copy_board)
            if opponent_best_score > best_score:
                best_score = opponent_best_score
                best_action = action
        return best_action 
    
    else:
        best_score = math.inf
        best_action = None
        
        for action in actions(board):
            copy_board = result(board, action)
            opponent_best_score = max_value(copy_board)
            if opponent_best_score < best_score:
                best_score = opponent_best_score
                best_action = action
        return best_action 
        
    
    