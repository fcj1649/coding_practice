
import math

max_d = 12000

ans = 0

for i in range(1, max_d + 1):
    for j in range(i // 3 + 1, (i - 1) // 2 + 1):
        if(math.gcd(i, j) == 1):            
            # print(i, j)
            ans = ans + 1

print(ans)