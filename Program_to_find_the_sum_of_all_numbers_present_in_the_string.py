s=str(input())
l=list(s)
p="123456789"
cnt=0
for i in range(0,len(l)):
    if l[i] in p:
        cnt+=int(l[i])
print(cnt)