import time

def inv_dig_sum(num:int, mod:int):
    quo = int(num // 9)
    rem = num % 9
    return ( rem * (10 ** quo)) + ((10 ** quo) - 1) % mod

out = 0
mod = 1000000007

f0 = 0
f1 = 1
current_big_S = 1
for i in range(2,91):
    f2 = f1 + f0
    #f2 is the current fib
    diff = f2 - f1
    big_S = current_big_S
    for j in range(f1+1,f2+1):
        big_S = ( big_S + inv_dig_sum(j, mod) ) % mod
    current_big_S = big_S
    f0 = f1
    f1 = f2

print(current_big_S % mod)

