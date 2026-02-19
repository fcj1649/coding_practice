m=1300000;q=[];n=[1]*m
for i in range(2,m):
    if(n[i]):
        q+=[i]
        j=i*i
        while(j<m):
            n[j]=0
            j+=i
for l in open(0):print(q[int(l)-1])