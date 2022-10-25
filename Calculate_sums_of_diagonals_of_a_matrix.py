n=int(input())
s1=0
s2=0
for i in range(0,n):
    a1=list(map(int,input().split()))
    s1=s1+a1[i]
    s2=s2+a1[len(a1)-1-i]
print("Principal Diagonal:",end="")
print(s1)
print("Secondary Diagonal:",end="")
print(s2)