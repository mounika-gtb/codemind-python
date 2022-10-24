a,b,c=map(int,input().split())
p,q,r=map(int,input().split())
al=0
bb=0
if a>p:
    al+=1
if a<p:
    bb+=1
if b>q:
    al+=1
if b<q:
    bb+=1
if c>r:
    al+=1
if c<r:
    bb+=1
print(al,bb)