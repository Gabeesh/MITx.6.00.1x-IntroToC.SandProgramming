'''
balance = 999999
annualInterestRate = 0.18

'''
balance = 320000; annualInterestRate = 0.2

mir = (annualInterestRate) / 12.0

l = (balance / 12.0)
u = (balance * ((1 + mir)**12.0))/12.0

count = 1
y = balance
i = 1
while True:
    #print count
    x = (l+u)/2
    while i < 13:
        RemaingBalance = balance - x
        balance = RemaingBalance + (RemaingBalance* (annualInterestRate/12))
        i+=1
    if balance < 0:
        u = x
    elif round(balance) == 0:
        print  'Lowest Payment:', round(x,2)
        break
    else:
        l = x
    count +=1
    i = 1
    balance = y


