"""
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is
3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO
people have won - assume that in every board there will only be one winner.
"""


def checkIfThereIsWinner(board):
    winner = None
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        winner = board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        winner = board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        winner = board[2][0]
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        winner = board[0][0]
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        winner = board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        winner = board[0][2]
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        winner = board[0][2]
    if winner == 0 or winner == ' ':
        winner = None
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 'no winner'
    return winner


if __name__ == '__main__':
    game = [[2, 1, 0],
            [1, 2, 0],
            [2, 0, 1]]

    print(checkIfThereIsWinner(game))