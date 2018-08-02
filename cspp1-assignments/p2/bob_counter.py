'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string
'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2'''

def main():
    ''' here we are finding the no of times the word
    bob has occured in a given string
    '''
    s_int = input()
    x_i = 0
    y_i = 1
    z_i = 2
    count_a = 0
    while z_i <= len(s_int):
        if s_int[x_i] == 'b' and s_int[y_i] == 'o' and s_int[z_i] == 'b':
            count_a += 1
        x_i += 1
        y_i += 1
        z_i += 1
    print(count_a)
    # the input string is in s
    # remove pass and start your code here
    

if __name__ == "__main__":
    main()
