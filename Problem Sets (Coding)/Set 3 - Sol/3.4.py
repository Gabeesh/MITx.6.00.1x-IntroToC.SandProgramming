def getAvailableLetters(lettersGuessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    list = []
    while i < len(string):
        list.append(string[i])
        i +=1
    #print list
    for x in lettersGuessed:
        list.remove(x)
    return ''.join(list)





lettersGuessed = ['z', 'w', 'd', 'n', 'v', 'x', 'b', 'e', 'o', 'a']
print getAvailableLetters(lettersGuessed)
