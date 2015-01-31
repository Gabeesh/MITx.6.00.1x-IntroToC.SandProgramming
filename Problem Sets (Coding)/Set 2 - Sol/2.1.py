balance = 4213
monthlyPaymentRate = 0.04
annualInterestRate = 0.2

i=1
sum = 0.0

while i < 13:
    print 'Month:',i
    Min_Mon_Payment = balance * monthlyPaymentRate
    print 'Minimum monthly payment:',round(Min_Mon_Payment,2)
    sum = sum + Min_Mon_Payment
    RemaingBalance = balance - Min_Mon_Payment
    #print 'Remaining balance:',RemaingBalance
    balance = RemaingBalance + (RemaingBalance* (annualInterestRate/12))
    print 'Remaining balance:',round(balance,2)
    i+=1

print 'Total paid:',round(sum,2)
print 'Remaining balance:',round(balance,2)

