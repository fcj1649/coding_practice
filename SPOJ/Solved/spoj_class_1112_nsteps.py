test_case = int(input())
for i in range(0, test_case):
    nums = input().split(" ")
    x = int(nums[0])
    y = int(nums[1])

    if(x == y):
        # x and y equal
        if( x % 2 == 0):
            #even
            print(x * 2)
        else:
            #odd
            print(x * 2 - 1)
    elif((x - y) == 2):
        # x and y sep by 2
        if( x % 2 == 0):
            #even
            print(x + y)
        else:
            #odd
            print(x + y - 1)
    else:
        print("No Number")