n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    s=s+l[i]
print(s)