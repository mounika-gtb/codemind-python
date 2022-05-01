n,k=map(int,input().split())
l=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,len(l)):
    if l[i]%k!=0:
        c+=1
print(c)
