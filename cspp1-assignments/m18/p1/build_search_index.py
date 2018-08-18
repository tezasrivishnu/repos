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
filename = "stopwords.txt"
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


# def word_list(text):
#     '''
#         Change case to lower and split the words using a SPACE
#         Clean up the text by remvoing all the non alphabet characters
#         return a list of words
#     '''

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

# def build_search_index(docs):
#     '''
#         Process the docs step by step as given below
#     '''

#     # initialize a search index (an empty dictionary)

#     # iterate through all the docs
#     # keep track of doc_id which is the list index corresponding the document
#     # hint: use enumerate to obtain the list index in the for loop

#         # clean up doc and tokenize to words list

#         # add or update the words of the doc to the search index

#     # return search index
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
    update = []
    for index in documents:
        update.append(index.split(','))
    # update_c = []
    # for index in update:
    #     for word in index:
    #         update_c[index][word].append(re.sub('[^ a-zA-z]', '', word.strip()))
    # print(update_c)
    update1 = []
    for index in update:
        for word in index:
            update1.append(word.lower().split())
    update1_copy = update1[:]
    for index in update1_copy:
        for word in index:
            if word in load_stopwords(filename):
                index.remove(word)
    dic ={}
    i = 0
    for index in update1_copy:
        for word in index:
            count = 0
            for char in index:
                if word == char:
                    count += 1
            if word in dic.keys():
                dic[word].append((i, count))
            else:
                dic[word] = [(i, count)]
        i += 1 
    print_search_index(dic)

if __name__ == '__main__':
    main()
