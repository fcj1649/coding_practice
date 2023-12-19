
def check_prime(input:str):
    num = int(input)
    i = 2
    while(i*i < num):
        if(num % i == 0):
            return False
        i+=1
    return True

def permute(out:list, current:str, input:str):
    if(len(input)<1):
        out.append(current)
    else:
        for i in range(len(input)):
            cur = input[i]
            next = current + cur
            rem = input[0:i]+input[i+1:]
            permute(out, next, rem)    

for i in reversed(range(2, 10)):
    input = ''
    for j in range(i):
        input += str(j+1)
    perm_act = []
    permute(perm_act, '', input)
    perm_act.sort(reverse=True)
    found = False
    for x in perm_act:
        if(check_prime(x)):
            print("Prime:"+x)
            found = True
            break
    if(found):
        break
            
        