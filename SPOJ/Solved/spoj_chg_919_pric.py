import math
def check_prime(input:int):
    num = int(input)
    i = 2
    while(i*i < num):
        if(num % i == 0):
            return False
        i+=1
    return True

mod = 2**31
a = 1
out = '0'
max_lim = 10**6
for i in range(max_lim):
    a = ( a + 1234567890 ) % mod
    if(check_prime(a)):
        out += '1'
    else:
        out += '0'
print(out)