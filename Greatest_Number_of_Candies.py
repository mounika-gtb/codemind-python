n=int(input())
l=list(map(int,input().split()))
e=int(input())
for i in range(0,len(l)):
    a1=l[i]
    a=l[i]+e
    l[i]=a
    if max(l)==l[i]:
        print("True",end=" ")
    else:
        print("False",end=" ")
    l[i]=a1
    