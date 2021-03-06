'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
FILE_NAME = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    lis = dict1.lower().split()
    lis1 = []
    for word in lis:
        lis1.append(re.sub('[^a-zA-Z]', '', word.strip()))
    temp1 = lis1[:]
    for word in temp1:
        if word in load_stopwords(FILE_NAME):
            lis1.remove(word)
    for word in lis1:
        if not word:
            lis1.remove(word)
    dic_t1 = {}
    for word in lis1:
        count = 0
        for char in lis1:
            if word == char:
                count += 1
        dic_t1[word] = count
    pis = dict2.lower().split()
    lis2 = []
    for word in pis:
        lis2.append(re.sub('[^a-zA-Z]', '', word.strip()))
    temp2 = lis2[:]
    for word in temp2:
        if word in load_stopwords(FILE_NAME):
            lis2.remove(word)
    for word in lis2:
        if not word:
            lis2.remove(word)
    dic_t2 = {}
    for word in lis2:
        count = 0
        for char in lis2:
            if word == char:
                count += 1
        dic_t2[word] = count
    key = set(list(dic_t2.keys()) + list(dic_t1.keys()))
    dic_t3 = {}
    for keys in key:
        dic_t3[keys] = [0, 0]
    for key in dic_t1:
        dic_t3[key][0] = dic_t1[key]
    for key in dic_t2:
        dic_t3[key][1] = dic_t2[key]
    numerator = 0
    for key in dic_t3:
        numerator += dic_t3[key][0]*dic_t3[key][1]
    dem1 = 0
    dem2 = 0
    for key in dic_t3:
        dem1 += dic_t3[key][0]**2
        dem2 += dic_t3[key][1]**2
    denominator = math.sqrt(dem1)*math.sqrt(dem2)
    similar = numerator/denominator
    return similar
def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(FILE_NAME, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
