n = 20
inp = [0] * (n + 1)

for i in range(1, len(inp)):
    inp[i] = i

for i in range(2, n+1):
    for j in range(i+1, n+1):
        if(inp[j] % inp[i] == 0):
            inp[j] = inp[j] // inp[i]

prod = 1
for i in range(1, len(inp)):
    prod *= inp[i]
print(inp, prod)