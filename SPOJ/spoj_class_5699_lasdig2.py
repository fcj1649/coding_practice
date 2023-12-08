def last_dig(base : int, power : int):
    ret = [[0], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6,4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
    
    if(power == 0):
        return 1
    else:
        bdig = base % 10
        pdig = power % len(ret[bdig])
        return ret[bdig][pdig]
    
def main():
    test_case = int(input())
    for i in range(0, test_case):
        nums = input().split(" ")
        print(str(last_dig(int(nums[0]), int(nums[1]))))

if __name__ == "__main__":
    main()