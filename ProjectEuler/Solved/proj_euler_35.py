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
out = [2,3,5,7]            
for i in range(11, len(list_num)):
    if(list_num[i]):
        #check circular
        isCircular = True
        dig = len(str(i))
        org = str(i)
        for j in range(1,dig):
            num = org[j:] + org[:j]
            if(not list_num[int(num)]):
                isCircular = False
        if(isCircular):
            out.append(i)
print(out)
print(len(out))
