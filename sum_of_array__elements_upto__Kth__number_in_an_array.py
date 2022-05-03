n=int(input())
l=list(map(int,input().strip().split()))[:n]
k=int(input())
sum=0
for i in range(0,len(l)):
    sum+=l[i]
    if l[i]==k:
        break
print(sum)
