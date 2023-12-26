import math
max_prime = 1000000
list_num = [0] * max_prime

list_num[0] = 0
list_num[1] = 0

for i in range(2, max_prime):
    if(list_num[i] == 0):
        j = i
        while( j < max_prime):
            list_num[j] += 1
            j = j + i
dig = 4
for i in range(len(list_num)-dig):
    if(i==644):
        pass

    if(list_num[i]==dig):
        isValid = True
        for j in range(dig-1):
            if(list_num[i+j+1]!=dig):
                isValid = False
                break
        if(isValid):
            print(i)
            break
