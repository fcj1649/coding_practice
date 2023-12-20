c = 0
b = 0
a = 0
max = 1000
m = 2
k = 2

out=[]
final_res = {}
while(a+b+c<=max):
    for n in range(1,m+1):
        a = m*m-n*n
        b = 2*m*n
        c = m*m+n*n
        if(a+b>c and b+c>a and c+a>b):
            sum_abc = a+b+c
            abc = [a,b,c]
            abc.sort()
            if abc not in out:
                out.append(abc)
                if sum_abc in final_res:
                    final_res[sum_abc] += 1
                else:
                    final_res[sum_abc] = 1
            #now generate k tuples
            for k in range(2,max+1):
                if(k*(sum_abc)>max):
                    break
                kabc = [k*a, k*b,k*c]
                kabc.sort()
                if kabc not in out:
                    out.append(kabc)
                    if k*sum_abc in final_res:
                        final_res[k*sum_abc] += 1
                    else:
                        final_res[k*sum_abc] = 1
        if(a+b+c >= max):
            break
    m+=1

print(dict(sorted(final_res.items(),key=lambda x:x[1],reverse=True)))
