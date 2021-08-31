# formula for calculating the interests
print('These are the formulas for calculating the interests')
print('Simple Interest = P × R × N where P=Principal amount R=Annual interest rate N=Term of loan in years')
print('Compound Interest = P [(1 + R)T – 1] where P=Principal amount R=Annual interest rate T=Number of years interest is applied')
print('')

# taking the values
print('Enter the values to get the interests')
principle = input('Enter the principle amount: ')
rate = input('Enter the rate of interest: ')
time = input('Enter the number of years of loan: ')
print('')

# simple interest
numerator = str(principle*rate*time)
simple = numerator/100
print('Simple Interest = ', simple)
print('')

# compound interest
pt1 = str((1 + rate)*time - 1)
pt1 -= 1
pt2 = str(principle*pt1)
print('Compound Interest = ', pt2)
print('')