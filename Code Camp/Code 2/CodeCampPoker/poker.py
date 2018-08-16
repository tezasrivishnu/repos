'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def sort(hand):
    '''
    appending face values into a list
    '''
    newlist = []
    for character in hand:
        if character[0] == 'A':
            newlist.append(14)
        elif character[0] == 'K':
            newlist.append(13)
        elif character[0] == 'Q':
            newlist.append(12)
        elif character[0] == 'J':
            newlist.append(11)
        elif character[0] == 'T':
            newlist.append(10)
        else:
            newlist.append(int(character[0]))
    return newlist

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    count = 0
    sor_lis = sorted(sort(hand))
    # print(sor_lis)
    for i in range(len(sor_lis)-1):
        if int(sor_lis[i+1]) - int(sor_lis[i]) == 1:
            count += 1
    if count+1 == len(sor_lis):
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
        set_ = set()
        for face, suite in hand:
            set_.add(suite)
        return
    '''
    char = hand[0][1]
    count = 0
    for character in hand:
        if character[1] == char:
            count += 1
    if count == len(hand):
        return True
    return False

        # for x, y in range(5):
        #     if lis[][y] == lis[][y+1]:
        #         return True
        #     else:
        #         return False

def is_fourofakind(hand):
    '''
    if the four face values in a hand are same then the hand will be four of a kind
    '''
    count = 0
    sor_lis = sorted(sort(hand))
    for i in range(len(sor_lis)-3):
        if sor_lis[i] == sor_lis[i+1] == sor_lis[i+2] == sor_lis[i+3]:
            count += 1
    if count == 1:
        return True
    return False

def is_threeofakind(hand):
    '''
    if the three face values in a hand are same then the hand will be three of a kind
    '''
    count = 0
    sor_lis = sorted(sort(hand))
    for i in range(len(sor_lis)-2):
        if sor_lis[i] == sor_lis[i+1] == sor_lis[i+2]:
            count += 1
    if count == 1:
        return True
    return False

def is_onepair(hand):
    '''
    if face values of one pair of cards in a hand is equal then hand is daid to be one pair
    '''
    sor_lis = sorted(sort(hand))
    set_list = set(sor_lis)
    if len(sor_lis) - len(set_list) == 1:
        return True
    return False

def is_twopair(hand):
    '''
    if face values of two pair of cards in a hand is equal then hand is daid to be one pair
    '''
    sor_lis = sorted(sort(hand))
    set_list = set(sor_lis)
    if len(sor_lis) - len(set_list) == 2:
        return True
    return False

def is_fullhouse(hand):
    '''
    three face values and two face values must be equal in a hand
    '''
    count = 0
    i = 0
    sor_lis = sorted(sort(hand))
    # for i in range(len(sor_lis)):
    if sor_lis[i] == sor_lis[i+1] == sor_lis[i+2] and sor_lis[i+3] == sor_lis[i+4]:
        count += 1
    elif sor_lis[i+3] == sor_lis[i+4] and sor_lis[i] == sor_lis[i+1] == sor_lis[i+2]:
        count += 1
    if count == 1:
        return True
    return False

def is_highcard(hand):

    new_lis = []
    for character in hand:
        if character[0] == 'A':
            new_lis.append(float(1.4))
        elif character[0] == 'K':
            new_lis.append(float(1.3))
        elif character[0] == 'Q':
            new_lis.append(float(1.2))
        elif character[0] == 'J':
            new_lis.append(float(1.1))
        elif character[0] == 'T':
            new_lis.append(float(1.0))
        else:
            new_lis.append(float(character[0]/10))
    return max(new_lis)

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_threeofakind(hand):
        return 3
    if is_onepair(hand):
        return 1
    if is_twopair(hand):
        return 2
    if is_fullhouse(hand):
        return 7
    if is_fourofakind(hand):
        return 4
    if is_flush(hand) and is_straight(hand):
        return 8
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    return is_highcard(hand)
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
