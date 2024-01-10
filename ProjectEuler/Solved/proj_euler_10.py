import math
max_prime = 2000000
list_num = [True] * max_prime

list_num[0] = False
list_num[1] = False

for i in range(2, max_prime):
    if(list_num[i]):
        j = i * i
        while( j < max_prime):
            list_num[j] = False
            j = j + i

sum_prime = 0
for idx, num in enumerate(list_num):
    if(num):
        sum_prime+= idx

print(sum_prime)