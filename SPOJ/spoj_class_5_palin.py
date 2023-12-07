import math

def copy_num(num : list, left : int, right: int):
    while( left >= 0 and right < len(num)):
        num[right] = num[left]
        left = left - 1
        right = right + 1
    return num

def next_palin(input: str):
    num = [int(i) for i in input]
    
    if(len(num) == 1):
        # only 1 digit the next palindrome is the next number if < 9 else if its 9 then 11
        if(num[0] == 9):
            num[0] = 1
            num.append(1)
        else:
            num[0] = num[0] + 1
    elif( len(num) % 2 == 0):
        # even number of digits
        mid = int(len(num) / 2)
        left = mid - 1
        right = mid

        suceess = False
        while( left >= 0 and right < len(num)):
            if(num[left] > num[right]):
                #left number is greater no need to change mid
                #copy all numbers from left to right
                num = copy_num(num, left, right)
                suceess = True
                break
            elif(num[left] < num[right]):
                #left number is smaller than right
                #add one to mid
                num[mid - 1] = num[mid - 1] + 1
                num[mid] = num[mid - 1]
                num = copy_num(num, left, right)
                suceess = True
                break
            else:    
                left = left - 1
                right = right + 1

        if(not suceess):
            # number is already a palindrome
            num[mid] = num[mid] + 1
            num[mid - 1] = num[mid - 1] + 1        
    else:
        # odd number of digits
        mid = math.floor(len(num) / 2)
        left = mid - 1
        right = mid + 1
        suceess = False
        while( left >= 0 and right < len(num)):
            if(num[left] > num[right]):
                #left number is greater no need to change mid
                #copy all numbers from left to right
                num = copy_num(num, left, right)
                suceess = True
                break
            elif(num[left] < num[right]):
                #left number is smaller than right
                #add one to mid

                # check if mid is 9
                if(num[mid] == 9):
                    num[mid] = 0
                else:
                    num[mid] = num[mid] + 1
                num = copy_num(num, left, right)
                suceess = True
                break
            else:    
                left = left - 1
                right = right + 1

        if(not suceess):
            # number is already a palindrome
            num[mid] = num[mid] + 1
    return "".join((str(x) for x in num))

def main():
    test_case = int(input())
    for i in range(0, test_case):
        print(next_palin(str(input())))

if __name__ == "__main__":
    main()