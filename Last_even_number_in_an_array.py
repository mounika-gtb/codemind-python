n=int(input())
l=list(map(int,input().strip().split()))[:n]
e=0
for i in range(0,len(l)):
   if l[i]%2==0:
      e=l[i]
print(e)

