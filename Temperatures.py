n=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    cnt=0
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            cnt=j-i
            break
    print(cnt,end=" ")