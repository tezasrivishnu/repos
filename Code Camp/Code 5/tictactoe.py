'''
    finding who's is the winner
'''
def mat(matrix):
    '''
    checking the possibilities
    '''
    temp = 0
    count = 0
    if (matrix[0][0] == matrix[1][0] == matrix[2][0] == "x"
            or matrix[0][1] == matrix[1][1] == matrix[2][1] == "x"
            or matrix[0][2] == matrix[1][2] == matrix[2][2] == "x"
            or matrix[0][0] == matrix[0][1] == matrix[0][2] == "x"
            or matrix[1][0] == matrix[1][1] == matrix[1][2] == "x"
            or matrix[2][0] == matrix[2][1] == matrix[2][2] == "x"
            or matrix[0][0] == matrix[1][1] == matrix[2][2] == "x"
            or matrix[0][2] == matrix[1][1] == matrix[2][0] == "x"):
        temp = 1
        count += 1
    if (matrix[0][0] == matrix[1][0] == matrix[2][0] == "o"
            or matrix[0][1] == matrix[1][1] == matrix[2][1] == "o"
            or matrix[0][2] == matrix[1][2] == matrix[2][2] == "o"
            or matrix[0][0] == matrix[0][1] == matrix[0][2] == "o"
            or matrix[1][0] == matrix[1][1] == matrix[1][2] == "o"
            or matrix[2][0] == matrix[2][1] == matrix[2][2] == "o"
            or matrix[0][0] == matrix[1][1] == matrix[2][2] == "o"
            or matrix[0][2] == matrix[1][1] == matrix[2][0] == "o"):
        temp = 2
        count += 1
    if count == 2:
        return 'invalid game'
    if temp == 1:
        return 'x'
    if temp == 2:
        return 'o'
    return 'draw'
def main():
    '''
    giving input to a program
    '''
    matrix = []
    flag = 0
    count_x = 0
    count_o = 0
    for i in range(3):
        matrix.append(input().split())
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "x" or matrix[i][j] == "o" or matrix[i][j] == ".":
                flag = 1
            else:
                flag = 0
            if matrix[i][j] == "x":
                count_x += 1
            elif matrix[i][j] == "o":
                count_o += 1
    if flag == 0:
        print("invalid input")
    elif count_x > 5 or count_o > 5:
        print("invalid game")
    else:
        print(mat(matrix))
if __name__ == '__main__':
    main()
