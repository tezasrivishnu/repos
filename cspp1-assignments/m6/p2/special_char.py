'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    we have to replace all the special character in a
    given string by a space
    '''
    str_input = input()
    for char in str_input:
        if char in "!@#$%^&*":
            str_input = str_input.replace(char," ")
    print(str(str_input))
if __name__ == "__main__":
    main()
