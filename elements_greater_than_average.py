n=int(input())
l=list(map(int,input().strip().split()))[:n]
s=0
c=0
for i in range(0,len(l)):
    s=s+l[i]
avg=s//n
for i in range(0,len(l)):
    if l[i]>=avg:
        c+=1
print(c)
