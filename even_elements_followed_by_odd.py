n=int(input())
l=list(map(int,input().strip().split()))[:n]
m=[]
for i in range(0,len(l)):
   if l[i]%2==0:
      m.append(l[i])
for i in range(0,len(l)):
   if l[i]%2!=0:
      m.append(l[i])
listtostring=' '.join(map(str,m))
print(listtostring)
