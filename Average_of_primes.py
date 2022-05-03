def fun(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count
n=int(int(input()))
l=list(map(int,input().strip().split()))[:n]
cf=0
c1=0
for i in range(0,len(l)):
    c=fun(l[i])
    if c==2:
        cf+=l[i]
        c1+=1
print("%.2f"%(cf/c1))
