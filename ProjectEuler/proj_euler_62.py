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
key = 5
cube_mapping = {}
cube_sort_map = {}
cube_sec_map = {}
for i in range(max_lim):
    cube = i ** 3
    cube_mapping[cube] = i
    cube_str = str(cube)
    cube_str = ''.join(sorted(cube_str.lstrip('0')))
    cube_sec_map[str(cube)] = cube_str
    if(cube_str in cube_sort_map):
        cube_sort_map[cube_str] += 1
    else:
        cube_sort_map[cube_str] = 1

for x,y in cube_sort_map.items():
    if(y == key):
        print(x, ' ', y)
        for a,b in cube_sec_map.items():
            if(b == x):
                print(a, ' ', b)
                break
        break