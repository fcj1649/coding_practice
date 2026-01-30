file = open('.\ProjectEuler\Solved\proj_euler_0022_names_new.txt', 'r')
tot_sum = 0
for line in file.readlines():
    names = line.strip().replace('"','').split(",")
    names.sort()
    tot_sum = 0
    for idx, name in enumerate(names):
        sum_val = 0
        for ch in name:
            if(ord(ch) >= 65 and ord(ch) <= 90):
                sum_val += ord(ch) - 64
        tot_sum += ( sum_val * (idx+1) )
print(tot_sum)
