a,b=list(map(int,input().split()))
op=0
if a==b+1 or a==b-1:
    op=1
elif a==10 and b==1:
    op=1
elif a==1 and b==10:
    op=1
else:
    op=0
if op==0:
    print("No")
else:
    print("Yes")
