import time
start_time = time.time()
start = 2
max_num = 10000
max_seq = -1
out = -1
out_seq = {}

for i in range(start,max_num):
    num = i
    while(num%2 == 0):
        num = int(num/2)
    while(num%5 == 0):
        num = int(num/5)
    init_num = num
    if(num > 1):
        #check if we already found a seq
        if(num in out_seq):
            len_seq = out_seq[num]
        else:
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
            
            len_seq = len(seq)
            out_seq[i] = len_seq    
        if(len_seq>max_seq):
            max_seq = len_seq
            out = i
print(out, max_seq)
end_time = time.time()
print('--- %s seconds ---' % (end_time-start_time))

# second approach
start_time = time.time()
max_prime = 10000 + 1
list_num = [True] * max_prime

list_num[0] = False
list_num[1] = False

for i in range(2, max_prime):
    if(list_num[i]):
        j = i * i
        while( j < max_prime):
            list_num[j] = False
            j = j + i

for i in range(start,max_num):
    num = i
    # check prime
    if(list_num[i]):
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
        len_seq = len(seq)
        if(len_seq>max_seq):
            max_seq = len_seq
            out = i

print(out, max_seq)
end_time = time.time()
print('--- %s seconds ---' % (end_time-start_time))                   
