'''
multiplication and addition of a matrix
'''
def mult_matrix(m_1, m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m_1) != len(m_2[0]):
        print("Error: Matrix shapes invalid for mult")
    else:
        mul_matrix = []
        for _ in range(len(m_1)):
            tem_matrix = []
            for _ in range(len(m_2[0])):
            #for z in range(len(b)):
                tem_matrix.append(0)
            mul_matrix.append(tem_matrix)
        for row_x in range(len(m_1)):
            for column_y in range(len(m_2[0])):
                for row_y in range(len(m_2)):
                    # print(row_x, column_y)
                    # print(row_x, row_y)
                    # print(row_y, column_y)
                    mul_matrix[row_x][column_y] += m_1[row_x][row_y] * m_2[row_y][column_y]
        return mul_matrix

def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m_1) != len(m_2):
        print("Error: Matrix shapes invalid for addition")
    else:
        addition_matrix = []
        for _ in range(len(m_1)):
            temp_matrix = []
            for _ in range(len(m_2[0])):
            #for z in range(len(b)):
                temp_matrix.append(0)
            addition_matrix.append(temp_matrix)
        for row in range(len(m_1)):
            for column in range(len(m_2[0])):
                addition_matrix[row][column] += m_1[row][column] + m_2[row][column]
        return addition_matrix
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    row, _ = input().split(',')
    for _ in range(int(row)):
        z_split = list(map(int, input().split()))
        matrix.append(z_split)
    return matrix


def main():
    '''
    intializing
    '''
    first_matrix = read_matrix()
    second_matrix = read_matrix()
    print(add_matrix(first_matrix, second_matrix))
    print(mult_matrix(first_matrix, second_matrix))

if __name__ == '__main__':
    main()
