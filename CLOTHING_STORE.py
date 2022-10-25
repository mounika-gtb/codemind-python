n=int(input())
arr=list(map(int,input().split()))
l=list(set(arr))
cnt=0
for i in range(0,len(l)):
    if arr.count(l[i])>=2:
        cnt+=(arr.count(l[i]))//2
print(cnt)