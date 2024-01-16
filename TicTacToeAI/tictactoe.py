"""
Tic Tac Toe Player
"""
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
    if not terminal(board):
        count_x = 0
        count_o = 0

        for row in board:
            for cell in row:
                if cell == X:
                    count_x += 1
                elif cell == O:
                    count_o += 1

        if count_x > count_o:
            return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if not board[row][col]:
                actions_set.add((row, col))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]]:
        raise NameError("It already has a value")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] and board[0][1] and board[0][2]:
        line = board[0][0] + board[0][1] + board[0][2]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O

    if board[1][0] and board[1][1] and board[1][2]:
        line = board[1][0] + board[1][1] + board[1][2]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O

    if board[2][0] and board[2][1] and board[2][2]:
        line = board[2][0] + board[2][1] + board[2][2]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O

    if board[0][0] and board[1][0] and board[2][0]:
        line = board[0][0] + board[1][0] + board[2][0]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O

    if board[0][1] and board[1][1] and board[2][1]:
        line = board[0][1] + board[1][1] + board[2][1]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O

    if board[0][2] and board[1][2] and board[2][2]:
        line = board[0][2] + board[1][2] + board[2][2]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O

    if board[0][0] and board[1][1] and board[2][2]:
        line = board[0][0] + board[1][1] + board[2][2]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O

    if board[0][2] and board[1][1] and board[2][0]:
        line = board[0][2] + board[1][1] + board[2][0]
        if line == "XXX":
            return X
        elif line == "OOO":
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for col in row:
            if not col:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    else:
        if player(board) == X:
            value, move = maxvalue(board)
            return move
        else:
            value, move = minvalue(board)
            return move


def maxvalue(board):
    v = float('-inf')
    if terminal(board):
        return utility(board), None

    move = None
    for action in actions(board):
        aux, act = minvalue(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move
    return v, move


def minvalue(board):
    v = float('inf')
    if terminal(board):
        return utility(board), None
    for action in actions(board):
        aux, act = maxvalue(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move
    return v, move
