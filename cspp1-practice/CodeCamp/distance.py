import re
import math
filename = "stopwords.txt"
def similarity(dict1, dict2):
    list_ = dict1.lower().split()
    list_1 = []
    for i in list_:
        list_1.append(re.sub('[^a-zA-Z]', '', i.strip()))
    temp_list = list_1[:]
    for i in temp_list:
        if i in load_stopwords(filename):
            list_1.remove(i)
    for i in list_1:
        if not i:
            list_1.remove(i)
    dict_1 = {}
    for i in list_1:
        count = 0
        for char in list_1:
            if i == char:
                count += 1
        dict_1[i] = count
    pis = dict2.lower().split()
    list_2 = []
    for i in pis:
        list_2.append(re.sub('[^a-zA-Z]', '', i.strip()))
    temp2 = list_2[:]
    for i in temp2:
        if i in load_stopwords(filename):
            list_2.remove(i)
    for i in list_2:
        if not i:
            list_2.remove(i)
    dict_2 = {}
    for i in list_2:
        count = 0
        for char in list_2:
            if i == char:
                count += 1
        dict_2[i] = count
    key = set(list(dict_2.keys()) + list(dict_1.keys()))
    dict_3 = {}
    for keys in key:
        dict_3[keys] = [0, 0]
    for key in dict_1:
        dict_3[key][0] = dict_1[key]
    for key in dic_t2:
        dict_3[key][1] = dic_t2[key]
    numerator = 0
    for key in dict_3:
        numerator += dict_3[key][0]*dict_3[key][1]
    denominator_1 = 0
    denominator_2 = 0
    for key in dict_3:
        denominator_1 += dict_3[key][0]**2
        denominator_2 += dict_3[key][1]**2
    denominator = math.sqrt(denominator_1)*math.sqrt(denominator_2)
    similarity = numerator/denominator
    return similarity
def load_stopwords(filename):
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
