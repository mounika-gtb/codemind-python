n=int(input())
l=list(map(int,input().strip().split()))[:n]
l1=list(set(l))
s=0
for i in range(0,len(l1)):
   if l.count(l1[i])==l1[i]:
      s+=1
print(s)
      
