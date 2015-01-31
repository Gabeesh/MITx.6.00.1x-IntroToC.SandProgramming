def getGuessedWord(secretWord, lettersGuessed):
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



secretWord = 'broccoli'
lettersGuessed = ['z', 'w', 'd', 'n', 'v', 'x', 'b', 'e', 'o', 'a']
print getGuessedWord(secretWord, lettersGuessed)
