def palindrome(n):
   sum=0
   while n:
      r=n%10
      sum=sum*10+r
      n=n//10
   return sum
n=int(input())
m=n
d1=palindrome(n)
for i in range(m-1,1,-1):
   d2=palindrome(i)
   if d2==i:
      c1=i
      break
for i in range(m+1,m+m):
   d3=palindrome(i)
   if d3==i:
      c2=i
      break
m1=m-c1
m2=c2-m
if m1<m2:
   print(c1)
elif m1>m2:
   print(c2)
elif m1==m2:
   print(c1,c2)
      
            
