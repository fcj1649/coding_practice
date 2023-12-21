import time
import math
length = 17201

max_num = ( length * length ) + 1
print( max_num * math.log(math.log(max_num)))

start_time = time.time()

list_num = [True] * max_num

list_num[0] = False
list_num[1] = False

for i in range(2, int(math.sqrt(max_num))):
    if(list_num[i]):
        j = i * i
        while( j < max_num):
            list_num[j] = False
            j = j + i
end_time = time.time()        
print('---%s seconds --- Prime generation for %s num' % (end_time-start_time,max_num))
start_time = time.time()

curr = 1
factor = 2
prime_count = 0
for i in range(3, length+1, 2):
    for j in range(4):
        curr += factor
        if(list_num[curr]):
            prime_count += 1
    factor += 2
end_time = time.time()
print(length, prime_count/((length * 2) - 1) * 100)
print('---%s seconds ---' % (end_time-start_time))