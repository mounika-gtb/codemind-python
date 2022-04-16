m,n=map(int,input().split())
for i in range(1,m+1):
   if m%i==0 and n%i==0:
      c=i
print(c)
