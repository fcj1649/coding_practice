import math
test_case = int(input())
for i in range(0, test_case):
    data = str(input())
    out = ""
    num = [int(i) for i in data]
    if(len(num) == 1):
        # only 1 digit the next palindrome is the next number if < 9 else if its 9 then 11
        if(num[0] == 9):
            num[0] = 1
            num.append(1)
        else:
            num[0] = num[0] + 1
    elif( len(num) % 2 == 0):
        # even number of digits
        out = ""
    else:
        # odd number of digits
        mid = math.floor(len(num) / 2)
        left = mid - 1
        right = mid + 1
        while( left >= 0 and right < len(num)):
            if(num[left] > num[right]):
                #left number is greater no need to change mid
                #copy all numbers from left to right
                left = left
            elif(num[left] < num[right]):
                #left number is smaller than right
                #add one to mid
                num[mid] = num[mid] + 1
            else:    
                left = left - 1
                right = right + 1
             

    out = out.join((str(x) for x in num))
    print(out)