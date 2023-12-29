
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

for i in range(3,max_prime,2):
    pass