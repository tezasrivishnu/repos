def character(hand):
    newlist = []
    for character in hand:
        if character[0] == 'A':
            newlist.append(0.14)
        elif character[0] == 'K':
            newlist.append(0.13)
        elif character[0] == 'Q':
            newlist.append(0.12)
        elif character[0] == 'J':
            newlist.append(0.11)
        elif character[0] == 'T':
            newlist.append(0.10)
        else:
            newlist.append(float(character[0])/100)
    return newlist
def handrank(hand):
    if flush(hand) and straight(hand):
        return 8
    if fullhouse(hand):
        return fullhouse(hand)
    if flush(hand):
        return 6
    if straight(hand):
        return 5
    if fourofakind(hand):
        return 4
    if threeofakind(hand):
        return 3
    if twopair(hand):
        return 2
    if onepair(hand):
        return onepair(hand)
    return highcard(hand)
def straight(hand):
    count = 0
    sortlis = sorted(character(hand))
    for i in range(len(sortlis)-1):
        if int(sortlis[i+1]) - int(sortlis[i]) == 1:
            count += 1
    if count+1 == len(sortlis):
        return True
    return False
def flush(hand):
    temp = hand[0][1]
    count = 0
    for character in hand:
        if character[1] == temp:
            count += 1
    if count == len(hand):
        return True
    return False
def fourofakind(hand):
    count = 0
    sortlis = sorted(character(hand))
    for i in range(len(sortlis)-3):
        if sortlis[i] == sortlis[i+1] == sortlis[i+2] == sortlis[i+3]:
            count += 1
    if count == 1:
        return True
    return False
def threeofakind(hand):
    count = 0
    sortlis = sorted(character(hand))
    for i in range(len(sortlis)-2):
        if sortlis[i] == sortlis[i+1] == sortlis[i+2]:
            count += 1
    if count == 1:
        return True
    return False
def twopair(hand):
    sortlis = sorted(character(hand))
    setlist = set(sortlis)
    if len(sortlis) - len(setlist) == 2:
        return True
    return False
def onepair(hand):
    sortlis = sorted(character(hand))
    newlis = []
    for i in sortlis:
        if sortlis.count(i) == 2:
            newlis.append(i)
    if len(newlis) == 0:
        return False
    maximum = max(newlis)
    return maximum + 1
def fullhouse(hand):
    i = 0
    sortlis = sorted(character(hand))
    newlis = []
    if sortlis[i] == sortlis[i+1] == sortlis[i+2] and sortlis[i+3] == sortlis[i+4]:
        newlis.append(sortlis[i])
    elif sortlis[i] == sortlis[i+1] and sortlis[i+2] == sortlis[i+3] == sortlis[i+4]:
        newlis.append(sortlis[i+2])
    if len(newlis) == 0:
        return False
    maximum = max(newlis)/100
    return maximum+7
def highcard(hand):
    newlis = sorted(character(hand))
    return max(newlis)
def poker(hands):
    return max(hands, key=handrank)
if __name__ == "__main__":
    COUNT = int(input())
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    print(' '.join(poker(HANDS)))

