n=int(input())
l=list(map(int,input().strip().split()))[:n]
o=0
for i in range(0,len(l)):
   if l[i]%2!=0:
      o=l[i]
print(o)

