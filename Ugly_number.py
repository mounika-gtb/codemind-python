def fun(n):
   c=0
   for i in range(1,n+1):
      if n%i==0:
         c+=1
   return c
n=int(input())#14
s=1
i=2
m=n
while n>1:#t
   d=fun(i)#2
   if d==2 and n%i==0:#t,
      s=s*i#2
      i=i#2
      n=n//i#7,
   elif d==2 and n%i!=0:
      i=i+1
   elif i>(n//i):
      break
if s==m:
   print("Ugly Number")
else:
   print("Not Ugly Number")
      
      
