def permute(out:list, current:str, input:str):
    if(len(input)<1):
        out.append(current)
    else:
        for i in range(len(input)):
            cur = input[i]
            next = current + cur
            rem = input[0:i]+input[i+1:]
            permute(out, next, rem)  

max_lim = 10 ** 6
key = 3
cube_mapping = {}
for i in range(max_lim):
    cube = i ** 3
    cube_mapping[cube] = i

for idx, val in enumerate(cube_mapping):    
    input = str(val)
    perm_act = []
    permute(perm_act, '', input)
    if(len(perm_act)>key):
        cube_count = 0
        for k in range(len(perm_act)):
            if(int(perm_act[k] in cube_mapping)):
                cube_count += 1
        if(cube_count == key):
            print(cube)
            break

