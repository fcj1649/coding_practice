import time

start_time = time.time()

seq = {1 : 1}
max = 1000000
max_seq = 1
out = 1
for i in range (2, max):
    # check if seq already exists
    count = 0
    num = i
    while(num != 1):
        if(num in seq):
            count = count + seq[num] - 1
            break
        else:
            count = count + 1

        if (num % 2 == 0):
            num = int(num / 2)
        else:
            num = 3 * num + 1
    
    seq[i] = count + 1
    if(count > max_seq):
        max_seq = count
        out = i
print(out)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))