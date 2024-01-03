import math
 
def primeFactors(n):
    prime_factor = {}
    while n % 2 == 0:
        if(2 in prime_factor):
            prime_factor[2] += 1
        else:
            prime_factor[2] = 1
        n = n // 2
         
    for i in range(3,int(math.sqrt(n))+1,2):         
        while n % i== 0:
            if(i in prime_factor):
                prime_factor[i] += 1
            else:
                prime_factor[i] = 1
            n = n // i

    if n > 2:
        if(n in prime_factor):
            prime_factor[n] += 1
        else:
            prime_factor[n] = 1
    return prime_factor
          
mod = 23
print(primeFactors(mod))
n = 34
print(primeFactors(n))
print(math.gcd(n, mod))
for i in range(1, 1000000):
    print(i, n * i % mod < n, n * i, n * i % mod)