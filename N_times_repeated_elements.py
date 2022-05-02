n=int(input())
l=list(map(int,input().strip().split()))[:n]
k=int(input())
l1=list(set(l))
s=0
for i in range(0,len(l1)):
   if k==l.count(l1[i]):
      print(l1[i],end=" ")
      s+=1
if s==0:
    print(-1)

