'''Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in
the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''
def main():
    '''
    we are finding the no of vowels in a given string
    '''
    s_int = input()
    count_i = 0
    for char in s_int:
        if char in 'aeiou':
            count_i += 1
    print(count_i)

    # the input string is in s
    # remove pass and start your code here


if __name__ == "__main__":
    main()
