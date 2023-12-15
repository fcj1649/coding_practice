import math

max = math.factorial(9) * 7
fact = [0] * 10
for i in range (0, 10):
    fact[i] = math.factorial(i)

sum = 0
for i in range(10, max):
    num = str(i)
    sumF = 0
    for j in range(len(num)):
        sumF += fact[int(num[j])]
    if(i == sumF):
        print(i)
        sum += i
print(sum)
