import sys
from sudoku import Sudoku

#check if the number if valid in the row and col and square
def is_valid(board, num, row, col):
    #test in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    #test in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    #test in the square
    corner_row = row - row % 3
    corner_col = col - col % 3

    for r in range(3):
        for c in range(3):
            if board[corner_row + r][corner_col + c] == num:
                return False

    return True

#solve the Puzzle
def suduko_solve(board, row, col):

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if board[row][col] > 0:
        return suduko_solve(board, row, col + 1)

    for num in range(1, 10):
        if is_valid(board, num, row, col):

            board[row][col] = num

            if suduko_solve(board, row, col + 1):
                return True

        board[row][col] = 0
    return False

#------------------- the cli app

sudokuBoard = [
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]
 ]
# function for import the data from file and store it in array
def solve(filename):
    print(f'\nSolve the Sudoku problem in file :  {filename}\n')

    with open(filename) as file:
        for line, i in zip(file, range(0, 9)):
            for  j in range(0, 9):
                sudokuBoard[i][j] = int(line.rstrip()[j])
    return True

#import data from the file
solve(sys.argv[1])
Sudoku(3, 3, board=sudokuBoard).show()
print("\n--- This is The Result ---\n")
suduko_solve(sudokuBoard, 0, 0)
Sudoku(3, 3, board=sudokuBoard).show()
