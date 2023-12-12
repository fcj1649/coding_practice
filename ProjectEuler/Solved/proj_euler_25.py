import math

def large_sum(list_1: list, list_2: list):
    list_out = []
    i = len(list_1)
    j = len(list_2)
    
    if(i > j):
        for x in range(i - j):
            list_2.insert(0, 0)
    elif(i < j):
        for x in range(j - i):
            list_1.insert(0, 0)
    
    carry = 0
    i = len(list_1) - 1
    j = len(list_2) - 1
    while(i>=0 and j>=0):
        sum = carry + list_1[i] + list_2[j]
        carry = int(sum / 10)
        list_out.insert(0, sum % 10)
        i -= 1
        j -= 1
    
    if(carry > 0):
        list_out.insert(0, carry)
    
    return list_out

n1 = [1]
n2 = [1]

n3 = []

seq = 2
while(len(n3) < 1000):
    seq = seq + 1
    n3 = large_sum(n2, n1)
    n1 = n2
    n2 = n3
    
print("".join(str(x) for x in n3))
print(seq)

