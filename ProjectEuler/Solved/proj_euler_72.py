max_den = 10 ** 6

totient_sum = [0.0] * (max_den + 1) 

for i in range(2, max_den+1):
    totient_sum[i] = float(i)

for i in range(2, max_den+1):
    if(totient_sum[i] == float(i)):
        totient_sum[i] = float(i - 1)
        j = i * 2
        while(j <= max_den):
            totient_sum[j] *= ( 1 - (1/i))
            j += i

print(totient_sum)

count = sum(totient_sum)

print(count)