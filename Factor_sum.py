def fun(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=i
    return c
op=[]
l=list((input().split(",")))
for j in range(0,len(l)):
    #print(fun(int(l[j])),end=" ")
    a=fun(int(l[j]))
    for p in range(0,len(l)):
        if str(a)==l[p]:
            op.append(l[j])
op.sort()
if len(op)==0:
    print("-1")
else:
    op1=" ".join(op)
    print(op1)
