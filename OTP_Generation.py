n=int(input())
n=str(n)
l=list(n)
op=[]
for i in range(0,len(l)):
    if int(l[i])%2!=0:
        op.append(str(int(l[i])**2))
op1="".join(op)
print(op1)