def fun(n):
   c=0
   for i in range(1,n+1):
      if n%i==0:
         c+=1
   return c
n=int(input())
c3=0
for i in range(1,n+1):
   if i*(n//i)==n:
      c1=fun(i)
      c2=fun(n//i)
      if c1==2 and c2==2:
         print(i,n//i)
         c3+=1
         break
      else:
         continue
if c3==0:
    print(-1)