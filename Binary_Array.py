n=int(input())
l=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,len(l)):
   if l[i]==0 or l[i]==1:
      continue
   else:
      c+=1
if c==0:
   print("True")
else:
   print("False")
