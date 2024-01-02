def sum_int(list_1: list, list_2: list):
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

def check_palin(input:list):
    is_palin = True
    i = 0
    j = len(input)-1
    while(i<j):
        if(input[i] != input[j]):
            is_palin = False
            break
        i+=1
        j-=1
    return is_palin

def rev_num(input:list):
    return input[::-1]

max_num = 10001
out = 0
for i in range(1, max_num):
    k = 0
    is_lych = True
    num = [int(x) for x in str(i)]
    while(is_lych and k < 50):
        rev = rev_num(num)
        sum_num = sum_int(num, rev)
        num = sum_num[:]
        is_lych = not check_palin(sum_num)
        k+=1
    print(i, is_lych, k, ''.join([str(x) for x in sum_num]))
    if(is_lych):
        out+=1
print(out)