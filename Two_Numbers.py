n=int(input())
a=list(map(int,input().split()))[:n]
o=[]
for i in range(0,len(a)):
    if a.count(a[i])==1:
        o.append(a[i])
o.sort()
print(o[0],o[1])
