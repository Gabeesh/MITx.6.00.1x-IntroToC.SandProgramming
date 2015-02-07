import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

#print loadWords()

word_list = loadWords()

hand =  {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}

word = 'rapture'

listy = []

for i in range(len(word)):
    listy.append(word[i])

print listy


flag = 0


for wordy in word_list:
    if word == wordy:
        print 'OKKKK'
        for x in listy:
            if x in hand:
                print hand[x]
                hand[x] -= 1
                if hand[x] < 0:
                   flag = 0
                   break
                else:
                    flag = 1

                continue
            else:
                flag = 0
                break
        break
    else:
        continue

print hand

if flag is 1:
    print 'OKKK',True
else:
    print False

