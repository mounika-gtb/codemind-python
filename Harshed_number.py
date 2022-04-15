n=int(input())
z=n
sum=0
while n:
   r=n%10
   sum=sum+r
   n=n//10
if z%sum==0:
   print("True")
else:
   print("False")
