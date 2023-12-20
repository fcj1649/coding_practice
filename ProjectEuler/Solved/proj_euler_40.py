base_seq =  '0123456789' 
champ_seq = '.123456789'
lim = 6
max_num = ( 10 ** lim )
j = 1
while(len(champ_seq) <= max_num):
    for x in base_seq:
        champ_seq = champ_seq + str(j) + str(x)
    j+=1

out = 1
for i in range(lim+1):
    dig = 10**i
    print(dig, champ_seq[dig])
    out = out * int(champ_seq[dig])

print(out)
print(champ_seq)