import math

def permute(out:list, current:str, input:str):
    if(len(input)<1):
        out.append(current)
    else:
        for i in range(len(input)):
            cur = input[i]
            next = current + cur
            rem = input[0:i]+input[i+1:]
            permute(out, next, rem)  

max_prime = 9999
list_num = [True] * max_prime

list_num[0] = False
list_num[1] = False

for i in range(2, max_prime):
    if(list_num[i]):
        j = i * i
        while( j < max_prime):
            list_num[j] = False
            j = j + i

for i in range(1000, max_prime):
    if(list_num[i]):
        perm_act = []
        input = str(i)
        permute(perm_act, '', input)
        perm_act = list(set(perm_act))
        perm_act.sort()
        perm_gre = []
        for k in range(len(perm_act)):
            if(int(perm_act[k]) >= i and list_num[int(perm_act[k])]):
                perm_gre.append(perm_act[k])
        if(len(perm_gre) >= 3):
            #print(i, perm_gre)
            first = perm_gre[0]
            for j in range(1,len(perm_gre)):
                second = perm_gre[j]
                diff = int(second) - int(first)
                # check if another terms
                for l in range(j+1,len(perm_gre)):
                    third = perm_gre[l]
                    if(diff == int(third) - int(second)):
                        print(first, second, third, diff)