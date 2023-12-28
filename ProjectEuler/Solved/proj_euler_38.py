def permute(out:list, current:str, input:str):
    if(len(input)<1):
        out.append(current)
    else:
        for i in range(len(input)):
            cur = input[i]
            next = current + cur
            rem = input[0:i]+input[i+1:]
            permute(out, next, rem)  

input = '987654321'
perm_act = []
permute(perm_act, '', input)
perm_act.sort(reverse=True)
for j in range(len(perm_act)):
    tot_len = 0
    for i in range(1,5):
        #check with 1,2,3 digit as 4 digit will need a min 12 chars
        curr = int(perm_act[j][0:i])
        tot_len = len(perm_act[j][0:i])
        seq = i
        k = 2
        isValid = True
        while(isValid and tot_len <9):
            next = curr * k
            k += 1
            next_len = len(str(next))
            tot_len += next_len
            if(str(next) != perm_act[j][seq:seq+next_len]):
                isValid = False
            seq = seq + next_len
        if(isValid):
            print(perm_act[j])
            break