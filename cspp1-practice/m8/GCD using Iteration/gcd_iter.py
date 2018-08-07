'''
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and
returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.
'''
def gcd_iter(a_i, b_i):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    #g_i = 1
    c_i = min(a_i, b_i)
    for i_i in range(c_i, 0, -1):
        if (a_i % i_i == 0) and (b_i % i_i == 0):
           # g_i = i_i
            break
    return i_i
def main():
    '''
    giving the input to find the gcd
    '''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
