def fun(n):
   c=0
   for i in range(1,n+1):
      if n%i==0:
         c+=1
   return c
n=int(input())
d1=fun(n)
sum=0
while n:
   r=n%10
   sum=sum*10+r
   n=n//10
d2=fun(sum)
if d1==2 and d2==2:
   print("circular prime")
elif d1==2 and d2!=2:
   print("prime but not a circular prime")
else:
    print("not prime")
