n=int(input())
b=bin(n)[2:]
a=list(b)
for i in range(0,len(a)):
    if a[i]=="0":
        a[i]="1"
    elif a[i]=="1":
        a[i]="0"
c="".join(a)
op=int(c,2)
print(op)
        