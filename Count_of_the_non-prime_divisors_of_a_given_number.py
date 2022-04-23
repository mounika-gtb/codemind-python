def fun(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
n=int(input())
s=0
for i in range(1,n+1):
    d=fun(i)
    if d!=2 and n%i==0:
       s+=1
print(s)
            
