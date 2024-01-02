# # need to generate prime - use sieve of eratosthenes
# import math
# import time
# start_time = time.time()
# max_prime = 10 ** 6 + 1
# list_num = [True] * max_prime

# list_num[0] = False
# list_num[1] = False

# for i in range(2, max_prime):
#     if(list_num[i]):
#         j = i * i
#         while( j < max_prime):
#             list_num[j] = False
#             j = j + i

# prime_no = []
# for i in range(len(list_num)):
#     if(list_num[i]):
#         prime_no.append(i)

# print("Prime generation done")

# def prime_factor_prod(num: int):
#     prime_factor_prod = float(num)

#     for j in range(len(prime_no)):
#         if(prime_no[j] <= num):
#             if(num % prime_no[j] == 0):
#                 prime_factor_prod *= (1 - (1 / float(prime_no[j])))
#                 while(num % prime_no[j] == 0):
#                     num = int(num/prime_no[j])
#         else:
#             break
#     return prime_factor_prod

# max_tot = 0.0
# out = 0
# for i in range(1, max_prime):
#     if(list_num[i]):
#         #number is prime, will have highest rel prime numbers
#         pass
#     else:
#         if(i % 100000 == 0):
#             print("Processing for %s completed" % i)

#         # get prime factors of a number
#         phi = prime_factor_prod(i)
#         if((i/phi) > max_tot):
#             out = i
#             max_tot = (i/phi)

# print(out, max_tot)
# end_time = time.time()
# print("--- %s --- seconds" % (end_time-start_time))
import time
start_time = time.time()
max_prime = 10 ** 6 + 1
prime_arr = [2,3,5,7,11,13,17,19, 23, 29, 31, 37]
out = prime_arr[0]
for i in range(1, len(prime_arr)):
    if(out * prime_arr[i]  >= max_prime):
        print(out, prime_arr[i])
        break
    else:
        out *= prime_arr[i]

end_time = time.time()
print("--- %s --- seconds" % (end_time-start_time))
