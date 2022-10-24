n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(0,len(l)):
    cnt=0
    for j in range(0,len(l)):
        if i!=j and l[j]<l[i]:
            cnt+=1
    print(cnt,end=" ")