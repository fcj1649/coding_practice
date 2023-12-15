max = 1000
max_dig = 10000000000

def powMod(base: int, power: int, mod: int):
    res = base
    for i in range(1,power):
        res = res * base % mod
    return res

sum = 0
for i in range(1,max+1):
    sum = sum + powMod(i,i,max_dig) 
    sum = sum % max_dig
print(sum)

