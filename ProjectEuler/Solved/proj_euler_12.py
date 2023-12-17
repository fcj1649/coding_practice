import math
import time
start_time = time.time()

limit = 76576500
n = 10000
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
prime_no = []
for i in range(len(list_num)):
    if(list_num[i]):
        prime_no.append(i)

no_of_div = 1
i = 1
out = 1
while(no_of_div < 500):
    tri_num = int((i * (i + 1)) / 2)
    out = tri_num

    no_of_div = 1 
    for j in range(len(prime_no)):
        if(prime_no[j] * prime_no[j] <= out):
            count_div = 0
            while(tri_num % prime_no[j] == 0):
                tri_num = int(tri_num / prime_no[j])
                count_div = count_div + 1
            if(count_div > 0):
                no_of_div = no_of_div * ( count_div + 1 )
            if(tri_num == 1):
                break
        else:
            break
    
    i += 1
print(out, no_of_div) 
end_time = time.time()
print("--- %s seconds ---" % ( end_time-start_time))
    