import math

def prime_generator(n:int):
    max_prime = n
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


max_prime = 10 ** 6

list_prime = prime_generator(max_prime)

start = 56003
end   = 56003

for i in range(start, end + 1):
    if(list_prime[i]):
        num = str(i)
        digits = list(map(int, num))
        
        # how many numbers to replace
        replace = []
        for k in range(1, len(digits)+1):
            # numbers
            for j in range(0, 10):
                replace.append(j)

                # position to replace
                for l in range(1, len(digits)-k+1):
                    digits_copy = digits[0:l-1] + replace + digits[l+k-1:]
                    print("position l:" + str(l) + " value k:" + str(k) + " "+ str(replace) + " result " + str(digits_copy))