'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    :params input dictionnary
    :return dict keys and values seperated by -
    '''
    dict_keys = sorted(list(dictionary.keys()))
    for _ in range(len(dict_keys)):
        print(str(dict_keys[_]) + " - " + str(dictionary[dict_keys[_]]))

def main():
    '''
    input- dict
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
