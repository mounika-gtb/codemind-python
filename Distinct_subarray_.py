n=int(input())
m=int(input())
d=[]
for i in range(n,m+1):
    d.append(i)
e=[]
cnt=0
for i in range(0,len(d)+1):
    for j in range(i+1,len(d)+1):
        e=d[i:j]
        if sum(e)%2!=0:
            cnt+=1
print(cnt)