n=int(input())
arr=list(map(int,input().split()))
k=int(input())
a=[]
while k!=0:
    a=[]
    d=arr[len(arr)-1]
    a.append(d)
    for i in range(0,len(arr)-1):
        a.append(arr[i])
    arr=a
    k=k-1
for i in range(0,len(a)):
    print(a[i],end=" ")