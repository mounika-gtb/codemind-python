def fun(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
m=int(input())
n=int(input())
for i in range(m,n+1):
    c=fun(i)
    if c==2:
        print(i)