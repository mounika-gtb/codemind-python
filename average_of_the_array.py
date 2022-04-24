n=int(input())
l=list(map(int,input().strip().split()))[ :n]
s=0
for i in range(0,len(l)):
    s=s+l[i]
s1=s/n
s2=round(s1,3)
print("%.2f"%s2)
