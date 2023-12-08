i=input
for _ in range(int(i())):print("%.5f"%sum(j/(pow(j,4)+pow(j,2)+1)for j in range(1,int(i())+1)))