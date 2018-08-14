def playHand(hand, wordList, n):
score = 0
    while calculateHandlen(hand) > 0:
        print('Current Hand:', end=' '); displayHand(hand)     
        guess = str(input('Enter word, or a "." to indicate that you are finished: '))        
        if guess == '.':        
            break            
        else:        
            if isValidWord(guess, hand, wordList) == False:            
                print('Invalid word, please try again.')
            else:
                score += getWordScore(guess, n)
                print(getWordScore(guess, n), "points. Total:", score, "points")
                
                hand = updateHand(hand, guess)               
    if guess == '.':
        print('Goodbye! Total score:', score, 'points.')
    else:
        print('Run out of letters. Total score:', score, 'points.')  