n,m=list(map(int,input().split()))
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
count=0
for i in range(0,len(b1)):
    if b1[i] in a1:
        a1.remove(b1[i])
    else:
        count+=1
        break
if count==0:
    print("Yes")
else:
    print("No")
    
        