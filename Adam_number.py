def fun(n):
   sum=0
   while n:
      r=n%10
      sum=sum*10+r
      n=n//10
   return sum
n=int(input())#12
d1=n*n#144
c1=fun(n)#21
d2=c1*c1#441
c2=fun(d2)#144
if d1==c2:
   print("True")
else:
   print("False")
