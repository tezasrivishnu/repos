'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    input - list
    return - dict
    '''
    dic = {}
    for index in range(len(string)):
        for word in string[index]:
            count = string[index].count(word)
            if word not in dic.keys():
                dic[word]  = count
    return dic
   
def main():
    '''
    input-  a number and integer
    output - dictionary
    '''
    input_number = int(input())
    list_input = []
    for _ in range(input_number):
        list_input.append(input().split())
    print(tokenize(list_input))

if __name__ == '__main__':
    main()
