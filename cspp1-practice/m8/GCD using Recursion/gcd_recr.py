'''
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in
two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.
'''
def gcd_recur(a_i, b_i):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a_i == 0:
        return b_i
    elif b_i == 0:
        return a_i
    else:
        return gcd_recur(b_i, a_i%b_i)
def main():
    '''
    giving input to find the gcd
    '''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
