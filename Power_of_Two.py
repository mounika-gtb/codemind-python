n=int(input())
i=0
c=0
while i<=n//2:
    r=1<<i
    if r==n:
        c=1
        print("True")
        break
    else:
        i+=1
if c==0:
    print("False")
    