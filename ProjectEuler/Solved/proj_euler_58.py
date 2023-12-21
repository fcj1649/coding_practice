import time, math

def isPrime(num:int):
    isPrime = True
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i == 0):
            isPrime = False
    return isPrime               

start_time = time.time()
length = 3
prime_count = 3
odd_count = 5
curr = 9
while(prime_count/odd_count >= 0.1):
    length += 2
    next = length - 1
    for j in range(4):
        curr += next
        if(isPrime(curr)):
            prime_count+=1
    odd_count += 4
print(length, prime_count/odd_count)    
end_time = time.time()    
print('---%s seconds ---' % (end_time-start_time))