# need to generate the 10001 st prime - use sieve of eratosthenes
import math

def prime_generator(n:int):
    max_prime = int(math.sqrt(n))
    list_num = [True] * max_prime

    list_num[0] = False
    list_num[1] = False

    for i in range(2, max_prime):
        if(list_num[i]):
            j = i * i
            while( j < max_prime):
                list_num[j] = False
                j = j + i
    return list_num

def largest_prime_factor(n:int, list_num:list):
    i = 2
    result = -1        
    while(i < len(list_num)):
        if(list_num[i]):
            while(n % i == 0):
                n = n // i
                result = i
        i += 1
    if(n != 1):
        return n
    else:
        return result        

n = 600851475143
list_num = prime_generator(n)
print(n, largest_prime_factor(n, list_num))
