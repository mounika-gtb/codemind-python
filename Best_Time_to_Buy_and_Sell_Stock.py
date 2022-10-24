n=int(input())
l=list(map(int,input().split()))
dif=0
#print(l)
for i in range(1,len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            a=abs(l[i]-l[j])
            if a>dif:
                dif=a
print(dif)
            
        