n=int(input())
l=list(map(int,input().strip().split()))[:n]
l1=list(set(l))
sum=0
for i in range(0,len(l1)):
     sum=sum+l1[i]
print(sum)

