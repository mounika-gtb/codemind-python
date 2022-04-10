n=int(input())
a,b=0,1
c=a+b
while c<=n:
   a=b
   b=c
   c=a+b
   if c==n:
      print("True")
      break
   else:
      continue
if c>n:
   print("False")
