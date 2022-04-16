n=int(input())
z=n
x=n
count=0
sum=0
while n:
   r=n%10
   count+=1
   n=n//10
while count!=0:
   r=z%10
   c=pow(r,count)
   sum=sum+c
   z=z//10
   count-=1
if sum==x:
   print("True")
else:
   print("False")
   
   
