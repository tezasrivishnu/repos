'''
    This is a continuation of the social network problem
    There are 3 functions below that have to be completed
    Note: PyLint score need not be 10/10 for this assignment. We expect 9.5/10
'''
def follow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the network dictionary and return it
    '''
    '''
    :params input---> a dict and two strings
    :returns a dict
    '''
    network_copy = network.copy()
    # for line in arg2:
    #     # key_split,val_split = line.split('follow')
    #     key_s, value_s = arg2.split()
    if arg1 in network_copy.keys():
        if arg2 not in network_copy[arg1]:
            network_copy[arg1].append(arg2)
    else:
        network_copy[arg1] = [arg2]
    return network_copy
def unfollow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        unfollow function is called when arg1 wants to stop following arg2
        so, this should result in removing arg2 from the followers list of arg1
        update the network dictionary and return it
    '''
    '''
    :params input---> a dict and two strings
    :returns a dict
    '''
    network_copy = network.copy()
    # map(lambda arg1: arg1.pop(arg2), network_copy)
    if arg1 in network_copy:
        if arg2 in network_copy[arg1]:
            network_copy[arg1].remove(arg2)
    return network_copy
def delete_person(network, arg1):
    '''
        2 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 is a person in the network
        delete_person function is called when arg1 wants to exit from the network
        so, this should result in deleting arg1 from network
        also, before deleting arg1, remove arg1 from the everyone's followers list
        update the network dictionary and return it
    '''
    '''
    :params input--->a dict and a string
    :returns a dict
    '''
    network_copy = network.copy()
    # for line in arg1:
    #     key_split = line.split('delete')
        # key_split = key_split.strip()
        # key_s = key_split
    if arg1 in network_copy.keys():
        for char in network_copy:
            if arg1 in network_copy[char]:
                network_copy[char].remove(arg1)
        del network_copy[arg1]
    return network_copy
def main():
    '''
        handling testcase input and printing output
    '''
    network = eval(input())
    lines = int(input())
    for i in range(lines):
        i += 1
        line = input()
        output = line.split(" ")
        if output[0] == "follow":
            network = follow(network, output[1], output[2])
        elif output[0] == "unfollow":
            network = unfollow(network, output[1], output[2])
        elif output[0] == "delete":
            network = delete_person(network, output[1])
    print(network)
if __name__ == "__main__":
    main()
