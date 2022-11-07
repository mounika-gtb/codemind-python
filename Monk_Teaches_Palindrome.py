def fun(s):
    n=s
    n1=s[::-1]
    if n==n1:
        return 1
    else:
        return 0
t=int(input())
for i in range(0,t):
    s=str(input())
    if fun(s)==True:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")