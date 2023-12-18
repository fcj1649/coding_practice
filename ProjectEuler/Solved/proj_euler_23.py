max = 10000
list_num = [True] * max

list_num[0] = False
list_num[1] = False

for i in range(2, max):
    if(list_num[i]):
        j = i * 2
        while( j < max):
            list_num[j] = False
            j = j + i
prime_no = []
for i in range(len(list_num)):
    if(list_num[i]):
        prime_no.append(i)

def prime_factor(num: int):
    prime_factor = {}

    for j in range(len(prime_no)):
        if(prime_no[j] <= num):
            while(num % prime_no[j] == 0):
                num = int(num/prime_no[j])
                if(prime_no[j] in prime_factor.keys()):
                    prime_factor[prime_no[j]] += 1
                else:
                    prime_factor[prime_no[j]] = 1
        else:
            break
    return prime_factor

def sum_of_divisor(num: int):
    out = 1
    for factor,count in prime_factor(num).items():
        out = int(out * ((factor ** (count+1) - 1)/(factor - 1)))
    return out - num

def main():
    max = 28123
    abund_list = []
    div_list = {}        
    for i in range(1, max+1):
        s_div = sum_of_divisor(i)
        div_list[i] = s_div
        if(i < s_div):            
            abund_list.append(i)
    
    sum_out = 0
    for i in range(1, max+1):
        j=0
        while(abund_list[j]<i):
            diff = i - abund_list[j]
            if(diff in abund_list):
                print(i, diff, abund_list[j])
                sum_out += i
                break
            j+=1

    sum_out = (max * (max + 1) / 2) - sum_out
    print(sum_out)

if __name__ == "__main__":
    main()