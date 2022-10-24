n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(0,len(l)):
    a=str(l[i])
    b=len(a)
    if b%2==0:
        cnt+=1
print(cnt)