n=int(input())
l=list(map(int,input().split()))
l.sort()
l=l[::-1]
#print(l)
for i in range(0,len(l)-1,2):
    d=str(l[i])
    l[i]=str(l[i+1])
    l[i+1]=str(d)
    #print(d)
#op=" ".join(l)
l[len(l)-1]=str(l[len(l)-1])
op=" ".join(l)
print(op)