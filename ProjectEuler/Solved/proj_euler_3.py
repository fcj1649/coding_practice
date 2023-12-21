# need to generate the 10001 st prime - use sieve of eratosthenes
import math
n = 600851475143
max = int(math.sqrt(n))
list_num = [True] * max

list_num[0] = False
list_num[1] = False

for i in range(2, max):
    if(list_num[i]):
        j = i * i
        while( j < max):
            list_num[j] = False
            j = j + i

i = max        
while(i > 0):
    i = i - 1
    if(list_num[i]):
        if(n % i == 0):
            print(i)
            break        