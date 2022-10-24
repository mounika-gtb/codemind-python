t=int(input())
for i in range(0,t):
    cnt=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        c=i%10
        if c==2 or c==3 or c==9:
            cnt+=1
    print(cnt)