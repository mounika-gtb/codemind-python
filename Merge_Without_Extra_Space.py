t=int(input())
for i in range(0,t):
    a,b=map(str,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1=l1+l2
    l1.sort()
    for i in range(0,len(l1)-1):
        print(l1[i],end=" ")
    print(l1[len(l1)-1],end="
")