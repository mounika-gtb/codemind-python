n=int(input())
l=list(map(int,input().strip().split()))[:n]
sum1=0
sum2=0
for i in range(0,n//2):
    sum1+=l[i]
for i in range(n//2,len(l)):
    sum2+=l[i]
if sum1>=sum2:
    print(sum1-sum2)
else:
    print(sum2-sum1)