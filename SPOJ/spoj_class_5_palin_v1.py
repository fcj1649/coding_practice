import math

def strComp(num1 : list, num2: list):
    if(len(num1) == len(num2)):
        for x in range(len(num1)):
            if(num1[x] == num2[x]):
                pass 
            else:
                return num1[x] > num2[x]
        # numbers are equal
        return False 
    else:
        return len(num1) > len(num2)
    
    return False

def copy_num(num : list, left : int, right: int):
    while( left >= 0 and right < len(num)):
        num[right] = num[left]
        left = left - 1
        right = right + 1

def next_palindrome(num: list, isEven : bool, mid: int, left: int, right : int):
    if(not isEven):
        if(num[mid] == 9):
            num[mid] = 0
            flag = True
            while(left >= 0 and right < len(num)):
                if(num[left]==9):
                    num[left] = num[right] = 0
                    left = left - 1
                    right = right + 1
                else:
                    num[left] = num[left] + 1
                    num[right] = num[right] + 1
                    flag = False
                    break
            if(flag):
                # number is 999 etc, make it 1001
                num[right - 1] = 1 
                num.insert(0, 1)
        else:                
            num[mid] = num[mid] + 1
    else:
        #number is even
        if(num[left] == 9):
            num[left] = 0
            num[right] = 0
            left = left - 1
            right = right + 1
            flag = True
            while(left >= 0 and right < len(num)):
                if(num[left]==9):
                    num[left] = num[right] = 0
                    left = left - 1
                    right = right + 1
                else:
                    num[left] = num[left] + 1
                    num[right] = num[right] + 1
                    flag = False
                    break
            if(flag):
                # number is 999 etc, make it 1001
                num[right - 1] = 1 
                num.insert(0, 1)
        else:
            num[left] = num[left] + 1
            num[right] = num[right] + 1
    return num

def next_palin_main(data_str: str):
    input_data   = [int(i) for i in data_str]
    palin_data  = input_data.copy()
    mid = int(math.floor(len(palin_data) / 2))
    if(len(palin_data) % 2 == 0):
        left = mid - 1
        right = mid
    else:
        left = mid - 1
        right = mid + 1

    copy_num(palin_data, left, right)
    out = ""

    if(not strComp(palin_data, input_data)):
        out = "".join((str(x) for x in next_palindrome(palin_data, (len(palin_data) % 2 == 0), mid, left, right )))
    else:
        out = "".join((str(x) for x in palin_data))
    return out


def main():
    test_case = int(input())
    for i in range(0, test_case):
        print(next_palin_main(str(input())))

if __name__ == "__main__":
    main()