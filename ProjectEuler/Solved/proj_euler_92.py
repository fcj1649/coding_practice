max_num = 10 ** 7
out = 0
seq_1 = [1,7,10,13,19,23,28,31,32,44,49,68,70,79,82,86,91,94,97,100]

for i in range(1, max_num):
    sum_sq_dig = sum((int(x)**2) for x in list(str(i)))
    while(len(str(sum_sq_dig)) > 2):
        sum_sq_dig = sum((int(x)**2) for x in list(str(sum_sq_dig)))
    if sum_sq_dig not in seq_1:
        out+=1
print(out)

# seq_1 = []
# seq_89 = []
# for i in range(1, max_num):
#     sum_sq_dig = i
#     curr_seq = []
#     while(True):
#         sum_sq_dig = sum((int(x)**2) for x in list(str(sum_sq_dig)))
#         if(sum_sq_dig in seq_1):
#             # will run to 1
#             seq_1.append(i)
#             break
#         elif(sum_sq_dig in seq_89):
#             # will run to 89
#             seq_89.append(i)
#             out+=1
#             break
#         else:
#             # new number
#             curr_seq.append(i)    
#             while(sum_sq_dig != 1 and sum_sq_dig != 89):
#                 curr_seq.append(sum_sq_dig)
#                 sum_sq_dig = sum((int(x)**2) for x in list(str(sum_sq_dig)))
#             if(sum_sq_dig == 1):
#                 # has run to 1
#                 # append all numbers in current sequence to 1
#                 seq_1.extend(curr_seq)
#                 break                
#             elif(sum_sq_dig == 89):
#                 # has run to 89
#                 seq_89.extend(x for x in curr_seq)
#                 out+=1
#                 break

# seq_1 = list(set(seq_1))
# seq_89 = list(set(seq_89))            
# print(seq_1)
# print(seq_89)
# print(out, len(seq_1), len(seq_89))

