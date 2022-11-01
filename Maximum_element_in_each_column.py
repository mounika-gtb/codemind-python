a,b=map(int,input().split())
d=[]
for i in range(0,a):
    l=list(map(int,input().split()))
    d.append(l)
p=[]
for i in range(0,b):
    p=[]
    for j in range(0,a):
        #print(d[j][i])
        p.append(d[j][i])
    print(max(p))

        
    