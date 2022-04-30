n=int(input())
l=list(map(int,input().strip().split()))[0:n]
c=int(input())
c1=0
for i in range(0,n):
   if l[i]==c:
      print("True")
      c1+=1
      break
if c1==0:
   print("False")

