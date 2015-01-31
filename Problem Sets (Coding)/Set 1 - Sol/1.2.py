s = raw_input("Pls give input string")

# bbobobboboboobobnwyubobbooboob
#print s.split('bob')
#print len(s.split('bob'))

x = s.find('bob')
#print s.find('bob')

count = 0
#print s[x+2:]

while x != -1:
    s = s[x+2:]
    #print s
    x = s.find('bob')
    count +=1
    #print x

print count

