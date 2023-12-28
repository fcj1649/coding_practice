import math
import time

start_time =  time.time()
max_prime = 10 ** 6
list_num = [True] * max_prime

list_num[0] = False
list_num[1] = False

for i in range(2, max_prime):
    if(list_num[i]): 
        j = i * i
        while( j < max_prime):
            list_num[j] = False
            j = j + i
prime_no = []            
for i in range(len(list_num)):
    if(list_num[i]):
        prime_no.append(i)

prime_sum = {}

for i in range(len(prime_no)):
    sum = prime_no[i]
    if(prime_no[i] not in prime_sum):
        prime_sum[prime_no[i]] = 1
    count = 1 
    for j in range(i+1, len(prime_no)):
        sum += prime_no[j]
        count += 1
        if(sum >= max_prime):
            break
        if(list_num[sum]):
            # sum is prime
            if(sum in prime_sum):
                prime_sum[sum] = max(count,prime_sum[sum])
            else:
                prime_sum[sum] = count
prime_sum = dict(sorted(prime_sum.items(), key=lambda x:x[1],reverse=True))
print(prime_sum.items())
end_time = time.time()
print("--- %s --- seconds" % (end_time-start_time))