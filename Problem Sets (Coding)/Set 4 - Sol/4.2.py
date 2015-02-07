hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = 'quail'

print len(word)

listy = []

nhand = hand.copy()
for i in range(len(word)):
    listy.append(word[i])

print listy

for x in listy:
    for k,v in nhand.items():
        if x == k:
            print x,k
            v -= 1
            print v
            nhand[k]=v

print nhand

print hand



