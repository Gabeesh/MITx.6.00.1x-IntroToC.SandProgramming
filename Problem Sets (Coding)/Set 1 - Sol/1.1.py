s = raw_input("Pls give the string")

count = 0
strlen = len(s)
i=0
while i < strlen:
    if s[i] == 'a' or s[i] == 'e'or s[i] == 'i'or s[i] == 'o'or s[i] == 'u':
        count += 1
    i=i+1

print count






