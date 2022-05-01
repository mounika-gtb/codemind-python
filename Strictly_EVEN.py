n=int(input())
l=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,len(l)):
   if l[i]%2==0:
      if i%2!=0:
         c+=1
      elif i%2==0:
         continue
if c>0:
   print("False")
elif c==0:
   print("True")
