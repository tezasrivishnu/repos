'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and
returns the sum of digits of given number.

# This function takes in one number and returns one number.
'''
l_ist = []
def sumofdigits(n_i):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_i == 0:
        return 0
    dig_it = n_i%10
    l_ist.append(dig_it)
    sumofdigits(n_i//10)
    fi_nal = sum(l_ist)
    return fi_nal
def main():
    '''
    giving input for to find the sum of digits
    '''
    a_i = input()
    print(sumofdigits(int(a_i)))
if __name__ == "__main__":
    main()
