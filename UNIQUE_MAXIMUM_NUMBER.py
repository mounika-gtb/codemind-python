n=int(input())
l=list(map(int,input().split()))
l1=list(set(l))
d=[]
for i in range(0,len(l1)):
    if l.count(l1[i])==1:
        d.append(l1[i])
if len(d)==0:
    print("-1")
else:
    print(max(d))