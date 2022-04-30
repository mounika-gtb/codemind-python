n=int(input())
l=list(map(int,input().strip().split()))[:n]
e=0
for i in range(0,len(l)-2):
   if l[i]%2!=0 and l[i+2]%2!=0:
       e+=1
print(e)

