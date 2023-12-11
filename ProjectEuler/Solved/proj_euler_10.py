# need to generate the 10001 st prime - use sieve of eratosthenes
import math
max = 2000000
list_num = [True] * max

list_num[0] = False
list_num[1] = False

for i in range(2, max):
    if(list_num[i]):
        j = i * 2
        while( j < max):
            list_num[j] = False
            j = j + i

sum = 0
for idx, num in enumerate(list_num):
    if(num):
        sum+= idx

print(sum)