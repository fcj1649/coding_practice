import math

def prime_sq_generator(n:int):
    max_prime = n
    list_num = [True] * max_prime

    list_num[0] = False
    list_num[1] = False

    list_prime_sq = []

    for i in range(2, max_prime):
        if(list_num[i]):
            j = i * i
            while( j < max_prime):
                list_num[j] = False
                j = j + i
    
    for i in range(len(list_num)):
        if(list_num[i]):
            list_prime_sq.append(i*i)
    
    return list_prime_sq



list_prime_sq = prime_sq_generator(10 ** 9)

out = []
for i in range(len(list_prime_sq)):
    num_str = str(list_prime_sq[i])
    rev_str = num_str[::-1]

    if(num_str != rev_str):
       # not a palin
       if(int(rev_str) in list_prime_sq):
           out.append(list_prime_sq[i])

print(out)
print(len(out))