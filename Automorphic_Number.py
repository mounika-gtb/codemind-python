n=int(input())
c=n**2
count=0
m=n
sum=0
hii=0
while n:
   r=n%10
   count=count+1
   n=n//10
for i in range(1,count+1):
   p=c%10
   sum=sum*10+p
   c=c//10
while sum!=0:
   z=sum%10
   hii=hii*10+z
   sum=sum//10
if hii==m:
   print("Automorphic Number")
else:
   print("Not an Automorphic Number")
   