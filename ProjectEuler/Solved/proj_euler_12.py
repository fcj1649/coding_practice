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
print(i, out, no_of_div) 
end_time = time.time()
print("--- %s seconds ---" % ( end_time-start_time))


def no_of_divisor(num:int):
    out = 1
    i = 2
    while(i * i <= num and num > 1):
        c = 0
        while(num % i == 0):
            num = num // i
            c += 1
        out = out * (c + 1)    
        i += 1
    if(num != 1):
        out = out * (1 + 1)
    return out
start_time = time.time()
max_div = 500
no_of_div = 1
i = 1
while(no_of_div < max_div):
    tri_num = i * (i+1) // 2
    no_of_div = no_of_divisor(tri_num)
    i+=1
print(i, tri_num, no_of_div)
end_time = time.time()
print("--- %s seconds ---" % ( end_time-start_time))


prime_arr = [2,3,5,7,11,13,17,19,23,29]
max_div = 500
