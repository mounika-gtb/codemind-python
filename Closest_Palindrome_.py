def fun(n):
    e=n
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if e==s:
        return 1
    else:
        return 0

n=int(input())
w=n
for i in range(n-1,0,-1):
    if fun(i)==1:
        op=i
        break
for i in range(n+1,n+n):
    if fun(i)==1:
        op1=i
        break
d=abs(op-w)
d1=abs(op1-w)
if d<d1:
    print(op)
elif d>d1:
    print(op1)
else:
    print(op,op1)