s=str(input())
d=s.split()
t1=[]
t2=[]
for i in range(0,len(d)):
   t1.append(min(d[i]))
   t2.append(max(d[i]))
b=min(t1)
c=max(t2)
print(b,end=" ")
print(s.count(b),end=" ")
print(c,end=" ")
print(s.count(c))
   
