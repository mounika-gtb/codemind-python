s=str(input())
l=list((s))
op=0
for i in range(0,len(l)):
    if l.count(l[i])==1:
        op=1
        print(i)
        break
if op==0:
    print("-1")