def fun(n):
   c=0
   for i in range(1,n+1):
      if n%i==0:
         c+=1
   return c
n=int(input())
c=fun(n)
if c==2:
   print(0)
else:
   for i in range(n-1,1,-1):
      m=fun(i)
      if m==2:
         r1=i
         break
   for i in range(n+1,n+10):
      h=fun(i)
      if h==2:
         r2=i
         break
   d1=n-r1
   d2=r2-n
   if d1>d2:
      print(d2)
   elif d1<d2:
      print(d1)
   elif d1==d2:
      print(d1)
        
