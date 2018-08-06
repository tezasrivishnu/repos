'''# Exercise: odd

# Write a Python function, odd, that takes in
one number and returns True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.
'''

def odd(x_i):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise
    '''
    return x_i%2 != 0
def main():
    '''
    we are giving input data
    '''
    data_i = input()
    print(odd(int(data_i)))

if __name__ == "__main__":
    main()
