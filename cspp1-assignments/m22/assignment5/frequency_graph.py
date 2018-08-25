'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
    :params input dictionnary
    :return dict keys and values seperated by -
    '''
    lis_ = sorted(dictionary)
    lis__ = []
    le_ = len(lis_)
    for key in range(le_):
        le_1 = len(str(dictionary[lis_[key]]))
        for _ in range(le_1):
            if dictionary[lis_[key]] == 1:
                lis__.append('#')
            if dictionary[lis_[key]] == 2:
                lis__.append('##')
    for _ in range(len(lis_)):
        print(str(lis_[_]) + " - " + str(lis__[_]))

def main():
    '''
    input
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
