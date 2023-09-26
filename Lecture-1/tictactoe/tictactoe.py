"""
Tic Tac Toe Player
"""

import math

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
    countX = 0
    countO = 0
    countEmpty = 0

    for row in board:
        for j in row:
            if j == "O":
                countO += 1
            elif j == "X":
                countX += 1
            else:
                countEmpty += 1
    
    if countEmpty == 9:
        return X
    if countX > countO:
        return O
    if countX == countO:
        return X





def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions  = []

    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            if row[j] == EMPTY:
                actions.append((i, j))
    return actions

                


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False


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
