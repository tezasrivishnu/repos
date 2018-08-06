'''
# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x),
that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.
'''
def evalQuadratic(a_i, b_i, c_i, x_i):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise
    '''
    return (a_i*(x_i**2) + b_i*x_i + c_i)

def main():
    '''
    input for calling evalquadratic function
    '''
    data_i = input()
    data_i = data_i.split(' ')
    data_i = list(map(float, data_i))
    # print(data_i)
    for x_i in range(len(data_i)):
        temp = str(data_i[x_i]).split('.')
        if temp[1] == '0':
            data_i[x_i] = int(float(str(data_i[x_i])))
        else:
            data_i[x_i] = data_i[x_i]
    print(evalQuadratic(data_i[0], data_i[1], data_i[2], data_i[3]))

if __name__ == "__main__":
    main()
