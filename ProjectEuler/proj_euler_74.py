import math
fact_list = []
for x in range(10):
    fact_list.append(math.factorial(x))

test_int = [169, 871, 872, 69, 78, 540]

final_count = 0

for x in range (10, 10 ** 6):
    num_loop = list()
    curr_num = x
    while curr_num not in num_loop:
        num_loop.append(curr_num)
        curr_num_dig = [int(i) for i in str(curr_num)]
        curr_num = 0
        for dig in curr_num_dig:
            curr_num = curr_num + fact_list[dig]
    if(len(num_loop) >= 60):
        print(x, len(num_loop))
        final_count = final_count + 1

print("final count", final_count)