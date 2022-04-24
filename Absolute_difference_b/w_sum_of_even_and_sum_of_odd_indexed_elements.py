n=int(input())
sum1=0
sum2=0
l=list(map(int,input().strip().split()))[ :n]
for i in range(0,len(l)):
   if i%2==0:
      sum1=sum1+l[i]
   else:
      sum2=sum2+l[i]
d=sum2-sum1
if d<0:
    print(-d)
else:
    print(d)

