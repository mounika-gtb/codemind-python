n=int(input())
c=0
sum=0
while n>0:
   r=n%10
   if r>c and sum<r:
      sum=r
   c=r
   n=n//10
print(sum)

