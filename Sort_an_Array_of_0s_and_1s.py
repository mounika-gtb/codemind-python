n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(0,len(l)):
    print(l[i],end=" ")