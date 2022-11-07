s=str(input())
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=1
for i in range(1,len(s)-1):
    if s[i] in a:
        c+=1
print(c)
        