def sumInt(list_1: list, list_2: list):
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

def prodInt(num1: list, num2:list):
    prod =[]
    j = len(num2) - 1
    while(j>=0):
        i = len(num1) - 1
        prod1 = [0] * ( len(num2) - 1 - j)
        carry = 0
        while(i>=0):
            prod1.insert( 0,  ( num1[i] * num2[j] + carry ) % 10)
            carry = int(( num1[i] * num2[j] + carry ) / 10)
            i-=1
        
        if(carry != 0):
            prod1.insert(0, carry)
        
        prod = sumInt(prod, prod1)
        j-=1
    return prod