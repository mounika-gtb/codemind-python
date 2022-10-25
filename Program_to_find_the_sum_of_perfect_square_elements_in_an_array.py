import math
def fun(n):
    e=n
    c=int(math.sqrt(n))
    c1=math.sqrt(n)
    if c==c1:
        return 1
    else:
        return 0
    

n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(0,len(arr)):
    if fun(arr[i])==1:
        s=s+arr[i]
print(s)