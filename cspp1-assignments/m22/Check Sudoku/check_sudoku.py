'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    k = len(sudoku)-1
    for i in range(9):
        if len(sudoku[i]) != len(set(sudoku[i])):
            return False
    for i in range(9):
        for j in range(8):
            if sudoku[j][i] == sudoku[j+1][i]:
                return False
    for i in range(8):
        if sudoku[i][i] == sudoku[i+1][i+1]:
            return False
    for i in range (8):
        if sudoku[i][k] == sudoku[i+1][k-1]:
            return False
    for i in range(1):
        for j in range(1):
            if (sudoku[i][j] == sudoku[i][j+1] == sudoku[i][j+2]
                == sudoku[i+1][j] == sudoku[i+1][j+1] == sudoku[i+1][j+2]
                == sudoku[i+2][j] == sudoku[i+2][j+1] == sudoku[i+2][j+2]):
            return False


    return True

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()