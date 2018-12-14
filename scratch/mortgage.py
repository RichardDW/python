# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:21:56 2017

@author: richard
"""

# Find out how long to pay off mortgage

principal = 500000
payment = 2525.00
rate = 0.05
total_paid = 0

# Extra payment info
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

out = open('mort_sched.txt', 'w')   # Open a file for writing

print('{:>5s} {:>10s} {:>9s} {:>10s}'.format('Month', 'Interest', 'Principal', 'Remaining'), file=out)
while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal * (rate / 12)
    principal = principal + interest - total_payment
    total_paid += total_payment
#    print(month, interest, total_payment - interest, principal)
    print('{:>4d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_payment - interest, principal), file=out)


print('\nTotal paid: {:>8.0f}'.format(total_paid), file=out)

out.close()

