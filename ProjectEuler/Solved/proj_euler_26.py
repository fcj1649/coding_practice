start = 2
max = 1000
max_seq = -1
out = -1

for i in range(start,max):
    num = i
    while(num%2 == 0):
        num = int(num/2)
    while(num%5 == 0):
        num = int(num/5)
    if(num > 1):
        # recurring
        # long division
        num = 1
        den = i
        seq = []
        rem_seq = []
        while(True):
            if(num < den):
                num *= 10
            quo = int(num/den)
            rem = num % den
            num = rem
            if(rem in rem_seq):
                # repeat
                # remove all elements before the first number to repeat
                seq.append(quo)
                idx = rem_seq.index(rem)
                seq=seq[idx+1:]
                break
            else:
                seq.append(quo)
                rem_seq.append(rem)
        if(len(seq)>max_seq):
            max_seq = len(seq)
            out = i
print(out, max_seq)
