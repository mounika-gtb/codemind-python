n=int(input())
l=list(map(int,input().split()))
a=l.count(0)
d=[]
#print(a)
for i in range(0,len(l)):
    if l[i]!=0:
        d.append(str(l[i]))
for i in range(0,a):
    d.append(str(0))
#print(d)
op=" ".join(d)
print(op)