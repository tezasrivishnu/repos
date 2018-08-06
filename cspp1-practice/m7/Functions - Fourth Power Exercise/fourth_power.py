'''
# Exercise: fourth power

# Write a Python function, fourthPower, that takes
in one number and returns that value raised to the fourth power.

# You should use the square procedure that you
defined in an earlier exercise exercise (you don't need to redefine square in this box;

# This function takes in one number and returns one number.
'''
def square(x_i):
    '''
    x_i: int or float.
    return output value as int or float
    '''
    return x_i*x_i

def fourthPower_i(x_i):
    '''
    x_i: int or float.
    return output value as int or float
    '''
    return square(x_i)*square(x_i)
def main():
    '''
    input for calling fourth power function
    '''
    data_i = input()
    data_i = float(data_i)
    temp = str(data_i).split('.')
    if temp[1] == '0':
        print(fourthPower_i(int(float(str(data_i)))))
    else:
        print(fourthPower_i(data_i))

if __name__ == "__main__":
    main()
