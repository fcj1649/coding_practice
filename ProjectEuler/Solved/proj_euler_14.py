import time

# start_time = time.time()

# seq = {1 : 1}
# max = 10 ** 6
# max_seq = 1
# out = 1
# for i in range (2, max):
#     # check if seq already exists
#     count = 0
#     num = i
#     while(num != 1):
#         if(num in seq):
#             count = count + seq[num] - 1
#             break
#         else:
#             count = count + 1

#         if (num % 2 == 0):
#             num = num // 2
#         else:
#             num = 3 * num + 1
    
#     seq[i] = count + 1
#     if(count > max_seq):
#         max_seq = count
#         out = i
# print(out)
# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))

def collatz_seq(seq_list: list, inp_num: int, max_list: list):
    out = max_list[len(max_list)-1]
    max_ret = seq_list[out]
    org_len = len(seq_list) 
    if (org_len <= inp_num):
        # sequence is not already processed
        # process the sequence
        for i in range(len(seq_list), inp_num+1):
            count = 0
            num = i
            while (num != 1):
                if (num % 2 == 0):
                    num = num // 2
                else:
                    num = 3 * num + 1
                if (num < len(seq_list)):
                    count = count + seq_list[num]
                    break
                else:
                    count += 1
            seq_list.append(count + 1)
            if (count + 1 >= max_ret):
                max_ret = count + 1
                out = i
            max_list.append(out)    
    return max_list[inp_num]
    
n = 15
start_time = time.time()                                
seq_list = [0, 1]        
max_list = [0, 1]

# print(collatz_seq(seq_list, 10 ** 6))
print("Euler Answer:", collatz_seq(seq_list, 10 ** 6, max_list))
print(collatz_seq(seq_list, 5 * 10 ** 6, max_list))
print(collatz_seq(seq_list, 10, max_list))
print(collatz_seq(seq_list, 15, max_list))
print(collatz_seq(seq_list, 20, max_list))
print(collatz_seq(seq_list, 1, max_list))    
#print(max_list)    
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
