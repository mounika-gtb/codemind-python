t=int(input())
for i in range(0,t):
    n=int(input())
    l=list(map(int,input().split()))
    s=n*(n+1)//2
    s1=sum(l)
    print(s-s1)