# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.

l = []
def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if(n==0):
        return l
    dig=n%10
    l.append(dig)
    sumofdigits(n//10)
    a = sum(l)
    return a
def main():
    a = input()
    print(sumofdigits(int(a)))  

if __name__== "__main__":
    main()

