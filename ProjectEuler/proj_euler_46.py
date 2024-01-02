
import math
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

for i in range(3,max_prime,2):
    if(not list_num[i]):
        #odd composite
        j = 0
        is_valid = False
        while(j < len(prime_no)):
            j+=1
            if(prime_no[j] > i - 2):
                break
            diff = i - prime_no[j]
            if( diff % 2 == 0):
                diff = int(diff / 2)
                root = math.sqrt(diff)
                if(root.is_integer()):
                    is_valid = True
                    break
        if(not is_valid):
            print(i)
            break



            

            
