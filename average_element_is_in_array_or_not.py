n=int(input())
l=list(map(int,input().strip().split()))[0:n]
c1=0
c2=0
for i in range(0,len(l)):
   c1+=l[i]
s=c1//n
for i in range(0,len(l)):
   if s==l[i]:
      print("True")
      c2+=1
      break
if c2==0:
   print("False")
