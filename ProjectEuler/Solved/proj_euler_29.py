import math

max_a = 100
max_b = 100
seq = []
for a in range(2,max_a+1):
    count = 0
    for b in range(2,max_b+1):
        num = a ** b
        if(num not in seq):
            count+=1
            seq.append(num)
    print(a, count)
print(len(seq))

# max_val = max(max_a+1, max_b+1)
# list_num = [True] * max_val

# list_num[0] = False
# list_num[1] = False

# for i in range(2, max_val):
#     if(list_num[i]):
#         j = i * 2
#         while( j < max_val):
#             list_num[j] = False
#             j = j + i

# out = 0
# for a in range(2,max_a+1):
#     prime_Factor = {}
#     num = a
#     while(num > 1):
#         for i in range(len(list_num)):
#             if(list_num[i]):
#                 if(num%i==0):
#                     num = int(num/i)
#                     if(i in prime_Factor):
#                         prime_Factor[i] += 1
#                     else:
#                         prime_Factor[i] = 1
#     gcd = 1  
#     for idx, fact in enumerate(prime_Factor):
#         if(idx == 0):
#             gcd = prime_Factor[fact]
#         else:
#             gcd = math.gcd(gcd, prime_Factor[fact])       
#     count = 0
#     if(gcd == 1):
#         count = max_b  - 1
#     else:
#         # get the gcdth root of a
#         j = 2
#         count = max_b  - 1
#         while(j <= gcd):
#             root = a ** (1 / j)
#             if(root.is_integer()):
#                 count -= int((max_b -1) / gcd)
#             j+=1
#     out+= count
#     print(a, count)
    
# print(out)

