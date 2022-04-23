def fun(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
n1=int(input())
n2=int(input())
i=1
while True:
    s=n1+n2+i
    if fun(s)==2:
        print(i)
        break
    i+=1
        
