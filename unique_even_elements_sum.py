n=int(input())
l=list(map(int,input().strip().split()))[:n]
l1=list(set(l))
c=0
for i in range(0,len(l1)):
    if l1[i]%2==0:
        c+=l1[i]
print(c)