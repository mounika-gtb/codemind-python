n=int(input())
l=list(map(int,input().strip().split()))[ :n]
s=l[0]
for i in range(1,len(l)):
    if l[i]>s:
        s=l[i]
print(s)

