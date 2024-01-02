def permute(out:list, current:str, input:str):
    if(len(input)<1):
        out.append(current)
    else:
        for i in range(len(input)):
            cur = input[i]
            next = current + cur
            rem = input[0:i]+input[i+1:]
            permute(out, next, rem)  

input = '0123456789'
perm_act = []
permute(perm_act, '', input)
final_perm = []
for perm in perm_act:
    if(perm[0] != '0' ):
        final_perm.append(perm)

final_perm.sort()

prime = [1,1,2,3,5,7,11,13,17]
out = []

for i in range(len(final_perm)):
    isValid = True
    for j in range(2,len(prime)):
        num_str = final_perm[i][j-1:j+2]
        if(len(num_str) == 3 and int(num_str) % prime[j] != 0):
            isValid = False
            break
    if(isValid):
        out.append(int(final_perm[i]))
print(out)
print(sum(x for x in out))
