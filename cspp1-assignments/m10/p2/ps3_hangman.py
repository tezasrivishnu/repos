# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os

WORDLIST_FILENAME = os.path.join('words.txt')

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            return True
        else:
            return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            output += secretWord[i]
        else:
            output += '_ '
    return output



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    output = ''
    alpha = string.ascii_lowercase
    for i in range(len(alpha)):
        if alpha[i] in lettersGuessed:
            output += ''
        else:
            output += alpha[i]
    return output
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistake = 0
    guess = 8
    lettersGuessed = ''
    wordguessed = False
    print('Welcome to the Hangman game.')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    while mistake < guess and not wordguessed:
        print('you have ' + str(guess - mistake) + ' available letters: ' + getAvailableLetters(lettersGuessed))
        print('-----------------------------------------')
        letter = input('please guess a letter: ')
        if letter in lettersGuessed:
            print("You already guessed" + getGuessedWord(secretWord, lettersGuessed))
            print('-----------------------------------------')
        else:
            lettersGuessed += letter
            if letter in secretWord:
                print('good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-----------------------------------------')
                if isWordGuessed(secretWord, lettersGuessed):
                    wordguessed = True
            else:
                print('letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-----------------------------------------')
                mistake += 1
    if wordguessed:
        print('Congratulations')
    else:
        print('Sorry! The word was ' + secretWord) 






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
