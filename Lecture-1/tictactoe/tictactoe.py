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
    i = action[0]
    j = action[1]

    newBoard = copy.deepcopy(board)
    moves = actions(newBoard)
    if action not in moves:
        raise NameError("Not a valid action")
    turn = player(board)
    if turn == X:
        turn = X
    else:
        turn = O

    newBoard[i][j] = turn

    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    tac = [X, O]
    rows = []
    for row in board:
        rows.append(row)
    columns = []
    for i in range(3):
        columns.append([board[0][i], board[1][i], board[2][i]])

    for tic in tac:
        # Horizontal victory:
        for row in rows:
            if row == [tic, tic, tic]:
                return tic
        # Vertical victory:
        for column in columns:
            if column == [tic, tic, tic]:
                return tic
        # Diagonal victory:
        if (board[1][1] == tic):
            if (board[0][0] == tic and board[2][2] == tic):
                return tic
            if (board[0][2] == tic and board[2][0] == tic):
                return tic
    return None





def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    if not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    def maxValue(board):
        value = -math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            value = max(value, minValue(result(board, action)))
        return value
    
    def minValue(board):
        value = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            value = min(value, maxValue(result(board, action)))
        return value
    
    
    
    if player(board) == X:

        if board == initial_state():
            return (1,1)

        moves = []
        for action in actions(board):
            moves.append([minValue(result(board, action)), action])
        value = -10
        selected = None
        for move in moves:
            if move[0] > value:
                value = move[0]
                selected = move
        return selected[1]

    else:
        moves = []
        for action in actions(board):
            moves.append([maxValue(result(board, action)), action])
        value = 10
        selected = None
        for move in moves:
            if move[0] < value:
                value = move[0]
                selected = move
        return selected[1]