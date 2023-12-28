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
max_prime = -1
out = (1,1)
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        prime_count = 0
        while(True):
            exp = n * n + n * a + b
            if(list_num[exp]):
                prime_count+=1
            else:
                if(prime_count > max_prime):
                    max_prime = prime_count
                    out = (a,b)
                break    
            n+=1
    print(a,b, prime_count)
print(out[0]*out[1], out, max_prime)
end_time = time.time()
print("--- %s --- seconds" % (end_time-start_time))