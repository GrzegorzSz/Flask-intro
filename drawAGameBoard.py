"""
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
(8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw,
and draw it for them to the screen using Python’s print statement.
"""


def drawLine(numOfCols):
    for col in range(numOfCols):
        print(' ---', end='')
    print('')


def drawColumns(numOfCols, rowOfVals = [' ', ' ', ' ']):
    print('|', end='')
    for col in range(numOfCols):
        if rowOfVals[col] == 0:
            rowOfVals[col] = ' '
        print(' %s |' % rowOfVals[col], end='')
    print('')


def drawBoard(cols, rows, board):
    for row in range(rows):
        drawLine(cols)
        drawColumns(cols, board[row])
    drawLine(cols)


def getBoardSize():
    y = input('Type number of rows: ')
    x = input('Type number of columns: ')
    if x.isnumeric() and y.isnumeric():
        return int(x), int(y)
    else:
        print('Board dimensions must be integers!')
        exit(1)

if __name__ == '__main__':
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    drawBoard(len(board), len(board[0]), board)

    # boardSize = getBoardSize()
    # drawBoard(boardSize[0], boardSize[1])
