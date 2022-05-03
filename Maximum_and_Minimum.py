n=int(input())
l=list(map(int,input().strip().split()))[:n]
l1=list(set(l))
s=0
t=[]
for i in range(0,len(l1)):
   if l1[i]==l.count(l1[i]):
      t.append(l1[i])
      s+=1
if s==0:
    print(-1)
print(min(t),max(t))

