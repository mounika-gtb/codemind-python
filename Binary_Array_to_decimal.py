n=int(input())
l=list(map(int,input().strip().split()))[:n]
sum=0
m=len(l)-1
for i in range(0,len(l)):
   sum=sum+(2**i)*l[m-i]
print(sum)
   
