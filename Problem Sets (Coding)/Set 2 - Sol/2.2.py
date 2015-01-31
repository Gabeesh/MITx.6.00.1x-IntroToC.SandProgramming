balance = 3926
annualInterestRate = 0.2

fixed = 0

x = balance
i = 1

while True:
    fixed = fixed + 10
    while i < 13:
        RemaingBalance = balance - fixed
        balance = RemaingBalance + (RemaingBalance* (annualInterestRate/12))
        i+=1
    #print balance
    if balance < 0:
        print  'Lowest Payment:', fixed
        break
    else:
        i = 1
        balance = x






