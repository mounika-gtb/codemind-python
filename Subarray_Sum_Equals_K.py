n,k=map(int,input().split())
l=list(map(int,input().split()))
d=[]
cnt=0
for i in range(0,len(l)+1):
    for j in range(i+1,len(l)+1):
        e=l[i:j]
        d.append(e)
        if sum(e)==k:
            cnt+=1
print(cnt)