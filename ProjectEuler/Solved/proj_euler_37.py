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
out = []
for i in range(11, max_prime):
    if(list_num[i]):
        dig = len(str(i))
        isTrunc = True
        for j in range(1,dig):
            num = str(i)[j:]
            if(not list_num[int(num)]):
                isTrunc = False
                break
            num = str(i)[:j]
            if(not list_num[int(num)]):
                isTrunc = False
                break
        if(isTrunc):
            out.append(i)
print(out)               
print(sum(x for x in out))        
        