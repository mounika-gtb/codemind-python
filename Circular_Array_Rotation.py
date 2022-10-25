n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
while k!=0:
    d=[]
    a=arr[len(arr)-1]
    d.append(a)
    for i in range(0,len(arr)-1):
        d.append(arr[i])
    arr=d
    k=k-1
for i in range(0,q):
    a=int(input())
    print(d[a])
    