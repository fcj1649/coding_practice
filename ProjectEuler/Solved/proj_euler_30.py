n = 6
max_num = (9 ** (n)) * (n+1)
out = 0
for i in range(2, max_num+1):
    numStr = str(i)
    sum_num = 0
    for j in range(len(numStr)):
        sum_num += int(numStr[j]) ** n
    if (i==sum_num):
        out += i
        # print(i)
print(out)