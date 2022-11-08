t=int(input())
for i in range(0,t):
    s=str(input())
    op=[]
    for i in range(0,len(s)-1):
        if s[i]!=s[i+1]:
            op.append(s[i])
    op1="".join(op)
    print(len(s)-len(op1)-1)
        