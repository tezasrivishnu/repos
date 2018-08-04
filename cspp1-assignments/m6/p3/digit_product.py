'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    product of all the digits in a mumber.
    '''
    s_i = input()
    l_i = list(s_i)
    i_i = 1
    p_i = 1
    while i_i+1 <= len(l_i):
        p_i *= l[i_i]*l[i_i+1]
        i_i += 2
    print(p_i)
if __name__ == "__main__":
    main()
