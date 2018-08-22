'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
file_name = "stopwords.txt"
# helper function to load the stop words from a file
def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    list_ = []
    characters = "@#$^&:/?><.,';"
    for var in characters:
        if var in text:
            text = text.replace(var, '')


    list_1 = text.lower().split()
    list_ = list(list_1)
    for word in list_:
        if word in load_stopwords(file_name):
            list_1.remove(word)
    return list_1

#     word_lis = text.copy()
#     update_lis = []
#     for index in word_lis:
#         update_lis.append(re.sub('[^a-zA-Z]', '', word.lower().strip()))
#     count = 0
#     word_dict = {}
#     for word in update_list:
#         for char in update_list:
#             if word ==  char:
#                 count += 1
#         word_dict[word_dict] = [(doc_id, count)]
#     return word_dict

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index

    dict_ = {}
    #print(docs)
    for lines in range(len(docs)):
        update_dict = word_list(docs[lines])
        for word in update_dict:
            if word not in dict_.keys():
                dict_[word] = [(lines, update_dict.count(word))]
            else:
                if (lines, update_dict.count(word)) not in dict_[word]:
                    dict_[word].append((lines, update_dict.count(word)))
    return dict_
    #     doc_copy = docs[:]
    #     dic = {}
    #     for index in doc_copy:
    #         word_list
# # helper function to print the search index
# # use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
        # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    print_search_index(build_search_index(documents))
    # update = []
    # for index in documents:
    #     update.append(index.split(','))
    # update_c = []
    # i = 0
    # for index in update:
    #     for word in index:
    #         update_c[i].append(re.sub('[^ a-zA-z]', '', word.strip()))
    #     i += 1
    # print(update_c)
    # update1 = []
    # i = 0
    # for index in update:
    #     for word in index:
    #         update1[i].append(word.lower().split())
    #     i += 1
    # update1_copy = update1[:]
    # i = 0
    # for index in update1_copy:
    #     print(index)
    #     for word in index:
    #         print(word)
    #         if word in load_stopwords(file_name):
    #             update1[i].remove(word)
    #     print(update1[i])
    #     i += 1
    # dic ={}
    # i = 0
    # for index in update1:
    #     for word in index:
    #         count = 0
    #         for char in index:
    #             if word == char:
    #                 count += 1
    #         if word in dic.keys():
    #             dic[word].append((i, count))
    #         else:
    #             dic[word] = [(i, count)]
    #     i += 1
    # print_search_index(dic)

if __name__ == '__main__':
    main()
