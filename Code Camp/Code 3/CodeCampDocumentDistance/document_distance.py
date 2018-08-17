import re
import math
filename = "C:/Users/itsvi/Desktop/MSIT/IT/CCSP 1/repo/Code Camp/Code 3/CodeCampDocumentDistance/stopwords.txt"
'''
    Document Distance - A detailed description is given in the PDF
'''
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
        if word in load_stopwords(filename):
            lis1.remove(word)
    for word in lis1:
        if len(word) == 0:
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
        if word in load_stopwords(filename):
            lis2.remove(word)
    for word in lis2:
        if len(word) == 0:
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
        dic_t3[keys] = [0,0]
    for key in dic_t1:
        dic_t3[key][0] = dic_t1[key]
    for key in dic_t2:
        dic_t3[key][1] = dic_t2[key]
    numerator = 0
    for key in dic_t3.keys():
        numerator += dic_t3[key][0]*dic_t3[key][1]
    dem1 = 0
    dem2 = 0
    for key in dic_t3.keys():
        dem1 += dic_t3[key][0]**2
        dem2 += dic_t3[key][1]**2
    denominator = math.sqrt(dem1)*math.sqrt(dem2)
    similarity = numerator/denominator
    return similarity
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
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
