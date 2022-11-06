s=str(input())
l=list(s)
for i in range(0,len(l)):
    if l[i]==".":
        l[i]="[.]"
op="".join(l)
print(op)
