SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

word = str(raw_input("Plese give the word"))
word = word.lower()
#print word

leng = len(word)

b = []

for i in range(len(word)):
    #print word[i]
    b.append(word[i])
    i +=1

a = []
a += word

#print a
#print b
#print leng
sum = 0
for i in range(leng):
    for k, v in SCRABBLE_LETTER_VALUES.iteritems():
        if k == b[i]:
            #print v ,
            sum = sum + v

#print "\n",(sum*leng)
n = 5
if leng == n:
    return ((sum*leng)+50)
else:
    return (sum*leng)