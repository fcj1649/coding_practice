from decimal import *
getcontext().prec = 1000000
euler = Decimal(1)
fact = 1
for i in range(1, 100):
    fact = fact * i 
    euler = euler + Decimal( 1 ) / Decimal( fact )

print(euler)
