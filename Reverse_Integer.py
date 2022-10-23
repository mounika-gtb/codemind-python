def fun(n):
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    return s

n=int(input())
if n>=0:
    print(fun(n))
else:
    print(-fun(-n))
    