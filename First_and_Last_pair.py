n=int(input())
l=list(map(int,input().strip().split()))[:n]
c=len(l)-1
if n%2==0:
    for i in range(0,n//2):
        print(l[i],l[c-i],end=" ")
elif n%2!=0:
    for i in range(0,len(l)//2):
        print(l[i],l[c-i],end=" ")
    print(l[n//2],0)
    