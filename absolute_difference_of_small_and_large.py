s=str(input())
d=s.split()
t1=[]
t2=[]
for i in range(0,len(d)):
   t1.append(ord(min(d[i])))
   t2.append(ord(max(d[i])))
for i in range(0,len(t1)):
    print(t2[i]-t1[i],end=" ")
   
