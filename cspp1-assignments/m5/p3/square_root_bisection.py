'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    ''' we have to find the square root of a given number 
    using bi-section methos
    '''
    s_in = int(input())
    epsilon_i = 0.01
    low_i = 0
    high_i = s_in
    ans_i = (low_i + high_i)/2
    while abs(ans_i**2 - s_in) >= epsilon_i:
        if ans_i**2 < s_in:
            low_i = ans_i
        else:
            high_i = ans_i
        ans_i = (low_i + high_i)/2
    print(ans_i)
if __name__ == "__main__":
    main()
