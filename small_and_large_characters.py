s=str(input())
d=s.split()
t1=[]
t2=[]
for i in range(0,len(d)):
   t1.append(min(d[i]))
   t2.append(max(d[i]))
for i in range(0,len(t1)):
    print(t1[i],t2[i],end=" ")
   
