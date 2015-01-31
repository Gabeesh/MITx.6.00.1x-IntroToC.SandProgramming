# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    newList = list(secretWord)
    flag = 0
    for x in newList:
        for y in lettersGuessed:
            if x == y:
                flag = 1
                break
            else:
                flag = 0
                continue
        if flag == 1:
            continue
        else:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    newList = list(secretWord)
    flag = 0
    final = []
    for x in newList:
        for y in lettersGuessed:
            if x == y:
                flag = 1
                break
            else:
                flag = 0
                continue
        if flag == 1:
            final.append(x)
            continue
        else:
            final.append('_')
            #return False
    #print final
    return ''.join(final)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    list = []
    while i < len(string):
        list.append(string[i])
        i +=1
    #print list
    for x in lettersGuessed:
        if x in list:
            list.remove(x)
    return ''.join(list)


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
    set = []
    i=0
    while i < len(secretWord):
        set.append(secretWord[i])
        i +=1
    print 'Welcome to the game, Hangman!'
    length = len(secretWord)
    print 'I am thinking of a word that is',length,'letters long.'
    print '-----------'
    i = 8
    flag = 1
    lettersGuessed = []
    guesslist = []
    while i>0:
        print 'You have',i,'guesses left.'
        print 'Available Letters:',getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter:')
        guessInLowerCase = guess.lower()
        lettersGuessed.append(guessInLowerCase)
        #guesslist.append(guess)
        #print lettersGuessed
        if guessInLowerCase in guesslist:
            print "Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed)
        elif guessInLowerCase in set:
            print 'Good guess:',getGuessedWord(secretWord, lettersGuessed)
        else:
            print "Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed)
            i -=1
        guesslist.append(guessInLowerCase)
        if isWordGuessed(secretWord, lettersGuessed):
            print '-----------'
            print 'Congratulations, you won!'
            flag = 0
            break
        print '-----------'
    if flag == 1:
        print 'Sorry, you ran out of guesses. The word was',secretWord,'.'








hangman('sea')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
