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

def main():
    file = open('.\ProjectEuler\proj_euler_13_input.txt', 'r')
    sum = []
    for line in file.readlines():
        num = [int(x) for x in line.strip()]
        sum = large_sum(num, sum)
                    
    print("".join((str(x) for x in sum)))
    print("".join((str(x) for x in sum))[0:10])

if __name__ == "__main__":
    main()