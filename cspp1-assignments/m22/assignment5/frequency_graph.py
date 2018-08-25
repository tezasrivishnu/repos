'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
    :params input dictionnary
    :return dict keys and values seperated by -
    '''
    dic = {}
    lis_ = sorted(dictionary)
    lis__ = []
    for key in range(len(lis_)):
        for values in range(dictionary[lis_[key]]):
            if dictionary[lis_[key]] == 1:
                lis__.append('#')
            if dictionary[lis_[key]] == 2:
                lis__.append('##')
    for _ in range(len(lis_)):
        print(str(lis_[_]) + " - " + str(lis__[_]))

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
