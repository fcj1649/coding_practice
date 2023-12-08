# Using readlines()
file1 = open('.\SPOJ\spoj_chg_378_sizecon.py', 'r')
Lines = file1.readlines()

# Strips the newline character
count = 0
for line in Lines:
    for x in line.strip():
        if(ord(x)) > 32:
            count += 1

print(count)