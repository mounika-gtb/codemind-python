t=int(input())
for i in range(0,t):
    n=int(input())
    s=str(input())
    l=list(s)
    op=0
    for i in range(0,len(l)):
        if l.count(l[i])==1:
            print(l[i])
            op=1
            break
    if op==0:
        print(-1)