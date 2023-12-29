# need to generate the 10001 st prime - use sieve of eratosthenes
import math
n = 10001
max_prime = math.ceil( n * ( math.log(n) + math.log(math.log( n )) ) )
list_num = [True] * max_prime

list_num[0] = False
list_num[1] = False

for i in range(2, max_prime):
    if(list_num[i]):
        j = i * i
        while( j < max_prime):
            list_num[j] = False
            j = j + i

i = 0        
for idx, num in enumerate(list_num):
    if(num):
        i = i + 1
        if( i == n):
            print(i, "th prime = ", idx)
        