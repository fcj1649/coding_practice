def math_spiral_sum(n:int):
    if(n==1):
        return 1
    else:
        curr = 0
        for i in range(1,5):
            curr += (i * (n-1)) + ((n-2)**2) 
        print(n, curr)
        return(curr + math_spiral_sum(n-2))
    
print(math_spiral_sum(1001))