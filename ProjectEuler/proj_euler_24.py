from itertools import permutations
perms = [''.join(p) for p in permutations('0123456789')]
perms.sort()
print(perms[1000000-1])
perm_act = []
def permute(out:list, current:str, input:str):
    if(len(input)<1):
        out.append(current)
    else:
        for i in range(len(input)):
            cur = input[i]
            next = current + cur
            rem = input[0:i]+input[i+1:]
            permute(out, next, rem)    
            
permute(perm_act, '', '0123456789')
perm_act.sort()
print(perm_act[1000000-1])