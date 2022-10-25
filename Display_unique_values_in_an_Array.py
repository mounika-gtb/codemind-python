n=int(input())
arr=list(map(int,input().split()))
l=list(set(arr))
d=[]
for i in range(0,len(l)):
    if arr.count(l[i])==1:
        d.append(str(l[i]))
if len(d)==0:
    print("-1")
else:
    op=" ".join(d)
    print(op)