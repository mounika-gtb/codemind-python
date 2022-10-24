n=int(input())
d=[]
cnt=0
for i in range(1,n+1):
    p=int(input())
    d.append(p)
t=int(input())
for i in range(0,len(d)):
    if d[i]<=t:
        cnt+=1
    else:
        cnt+=2
print(cnt)
    