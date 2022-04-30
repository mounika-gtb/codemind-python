n=int(input())
l=list(map(int,input().strip().split()))[0:n]
c=int(input())
c1=0
for i in range(0,len(l)):
   if c==l[i]:
      c1+=1
print(c1)
