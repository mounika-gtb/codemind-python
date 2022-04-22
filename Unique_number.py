n=int(input())
m=n
l=[]
c=0
while n:
   r=n%10
   l.append(r)
   n=n//10
while m:
   m=m//10#123
   r1=m%10#3
   
   for i in range(0,len(l)):
      if l[i]==r1:
         c+=1
if c>len(l):
   print("Not Unique Number")
elif c<=len(l):
   print("Unique Number")
