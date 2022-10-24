n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(0,len(l)):
    q=l[i]*l[i]
    d.append(q)
d.sort()
for i in range(0,len(d)):
    print(d[i],end=" ")