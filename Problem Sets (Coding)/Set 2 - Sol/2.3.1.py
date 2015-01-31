'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

'''
balance = 999999
annualInterestRate = 0.18


mir = (annualInterestRate) / 12.0

l = (balance / 12.0)
u = (balance * ((1 + mir)**12.0))/12.0

epsilon = 0.01
count = 1
y = balance
i = 1
while True:
    print count
    x = (l+u)/2
    while i < 13:
        RemaingBalance = balance - x
        balance = RemaingBalance + (RemaingBalance* (annualInterestRate/12))
        #print balance
        i+=1
    #if abs(balance - x) <= epsilon:
    if balance < 0:
        u = x
        #print  'Lowest Payment:', round(x)
        #print count
    elif round(balance) == 0.1:
        print  'Lowest Payment:', round(x)
        break
    else:
        l = x
    count +=1
    i = 1
    balance = y


