n=int(input())
l=list(map(int,input().split()))
d=list(set(l))
e=[]
for i in range(0,len(d)):
    a=l.count(d[i])
    e.append(a)
f=max(e)
for i in range(0,len(d)):
    if l.count(d[i])==f:
        print(d[i])
        break
    