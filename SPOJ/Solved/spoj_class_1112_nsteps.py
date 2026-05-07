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

"""
XC	YC	X+y	x-y	X-E/O	No	%4
0	0	0	0	EVEN	0	0
1	1	2	0	ODD	    1	1
2	0	2	2	EVEN	2	2
3	1	4	2	ODD	    3	3
2	2	4	0	EVEN	4	0
3	3	6	0	ODD	    5	1
4	2	6	2	EVEN	6	2
5	3	8	2	ODD	    7	3
4	4	8	0	EVEN	8	0
5	5	10	0	ODD	    9	1
6	4	10	2	EVEN	10	2
7	5	12	2	ODD	    11	3
6	6	12	0	EVEN	12	0
7	7	14	0	ODD	    13	1
"""