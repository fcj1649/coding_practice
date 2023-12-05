# need to generate the 10001 st prime - use sieve of eratosthenes
import math
n = 10001
max = math.ceil( n * ( math.log(n) + math.log(math.log( n )) ) )
list_num = [True] * max

list_num[0] = False
list_num[1] = False

for i in range(2, max):
    if(list_num[i]):
        j = i * 2
        while( j < max):
            list_num[j] = False
            j = j + i

i = 0        
for idx, num in enumerate(list_num):
    if(num):
        i = i + 1
        if( i == n):
            print(i, "th prime = ", idx)
        