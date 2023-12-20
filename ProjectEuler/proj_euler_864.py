import math
n = 10
max = n * n + 1
list_num = [True] * max

list_num[0] = False
list_num[1] = False

for i in range(2, max):
    if(list_num[i]):
        j = i * 2
        while( j < max):
            list_num[j] = False
            j = j + i
        

def check_square_Free(num: int):
    pass



for i in range(1,n+1):
    print(i*i+1)