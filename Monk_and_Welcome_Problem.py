a=int(input())
l1=list(map(str,input().split()))
l2=list(map(str,input().split()))
op=[]
for i in range(0,len(l1)):
    b=int(l1[i])+int(l2[i])
    op.append(str(b))
op1=" ".join(op)
print(op1)