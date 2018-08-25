'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    '''
    removing the special characters
    :params input--string
    return- a string
    '''
    list_input = []
    char_acters = "!@#$%^&*()_-+=:' ;<>,./?"
    for char in string:
        if char not in char_acters:
            list_input.append(char)
    return ''.join(list_input)


def main():
    '''
    giving the input  as a string
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
