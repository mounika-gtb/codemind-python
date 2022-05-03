n=int(input())
l=list(map(int,input().strip().split()))[:n]
l1=list(set(l))
s=0
sum=0
for i in range(0,len(l1)):
   if l1[i]==l.count(l1[i]):
      sum+=l1[i]
      s+=1
if s==0:
    print(-1)
c=sum/s
print("%.2f"%c)

