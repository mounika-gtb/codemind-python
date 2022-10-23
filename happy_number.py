def fun(n):
    s=0
    e1=n
    while e1!=0:
        r=e1%10
        s=s+(r*r)
        e1=e1//10
    return s
n=int(input())
e=n
a=n
while len(str(a))>1:
    a=fun(n)
    n=a
if a==1:
    print("True")
else:
    print("False")