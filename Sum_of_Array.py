n=int(input())
sum1=0
l=list(map(int,input().strip().split()))[ :n]
for i in range(0,len(l)):
    sum1=sum1+l[i]
print(sum1)
 

