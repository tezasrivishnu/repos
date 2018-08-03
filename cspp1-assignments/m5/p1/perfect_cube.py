'''
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
'''
def main():
    '''we have to find out whether the given number is perfect
    cube or not
    '''
    s_in = int(input())
    ans_c = 0
    while ans_c**3 < abs(s_in):
        ans_c = ans_c + 1
    if ans_c**3 != abs(s_in):
        print(str(s_in) + " is not a perfect cube")
    else:
        if s_in < 0:
            ans_c = -ans_c
        print(str(s_in) + " is a perfect cube")
if __name__ == "__main__":
    main()
