m=int(input())
n=int(input())
s=0
for i in range(1,m+1):
    l=list(map(int,input().split()))
    s=s+sum(l)
print(s)
    