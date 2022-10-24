n=int(input())
l=list(map(int,input().split()))
d=list(set(l))
for i in range(0,len(d)):
    print(d[i],end=" ")