'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    '''
    here we are finding the square root of a number using
    newton-rampson method
    '''
    s_in = int(input())
    epsilon_c = 0.01
    guess_g = s/2.0
    nguess_g = 0
    while (guess_g*guess_g-s_in) >= epsilon_c and guess_g <= s_in:
        nguess_g += 1
        guess_g = guess_g - (((guess_g**2) - s)/(2*guess_g))
    print(guess_g)
if __name__ == "__main__":
    main()
