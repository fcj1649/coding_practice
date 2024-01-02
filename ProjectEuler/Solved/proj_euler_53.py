

# for n in range(1,101):
#     r = 1
#     while(r<=int(n/2)):

max_lim = 10 ** 6
out = 0
for n in range(1,101):
    r = 1
    while(r<=n):
        num = [i for i in reversed(range(1,n+1))]
        den = [i for i in reversed(range(1,r+1))]
        den.extend([i for i in reversed(range(1,n-r+1))])
        
        for i in range(len(num)):
            #check if num exists in den
            if(num[i] in den):
                den[den.index(num[i])] = 1
                num[i] = 1

        prod = 1
        for i in range(len(num)):
            prod *= num[i]

        for i in range(len(den)):
            prod /= int(den[i])    

        if(prod > max_lim):
            out+=1
            print(n, r, prod)
        r+=1
print(out)