'''
# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two
arguments a character and String and returns the isIn(char, aStr)
which retuns a boolean value.
# This function takes in two arguments character and String and
returns one boolean value.
'''
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
        returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    elif len(aStr) == 1 and aStr == char:
        return True
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[len(aStr)//2] == char:
        return True
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[(len(aStr)//2):])
    return isIn(char, aStr)
def main():
    data = input()
    data = data.split()
    print(isIn((data[0]), data[1]))
if __name__ == "__main__":
    main()
