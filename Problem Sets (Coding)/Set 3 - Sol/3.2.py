def isWordGuessed(secretWord, lettersGuessed):
    newList = list(secretWord)
    flag = 0
    #print newList
    for x in newList:
        #print x
        for y in lettersGuessed:
            #print y
            if x == y:
                flag = 1
                break
            else:
                flag = 0
                continue
        #print '0k'
        if flag == 1:
            #print 'ook'
            continue
        else:
            #print 'Test'
            return False
    return True



secretWord = 'broccoli'
lettersGuessed = ['z', 'w', 'd', 'n', 'v', 'x', 'b', 'e', 'o', 'a']
print isWordGuessed(secretWord, lettersGuessed)

''''
newList = list(secretWord)

print newList

'''