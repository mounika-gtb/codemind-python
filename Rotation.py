

t=int(input())
for i in range(0,t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    while k!=0:
        d=[]
        
        d.append(str(arr[len(arr)-1]))
        for i in range(0,len(arr)-1):
            d.append(str(arr[i]))
        k=k-1
        arr=d
    op=" ".join(d)
    print(op)