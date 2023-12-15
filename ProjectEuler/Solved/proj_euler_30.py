import math
max = int(math.pow(9,5) * 6)
out = 0
for i in range(2,max+1):
    numStr = str(i)
    sum = 0
    for j in range(len(numStr)):
        sum += math.pow(int(numStr[j]),5)
    if(i==sum):
        out += i
        print(i)
print(out)