n=int(input())
sum=0
l=list(map(int,input().strip().split()))[ :n]
for i in range(0,len(l)):
   if l[i]%2==0:
      continue
   else:
      sum=sum+l[i]
print(sum)

