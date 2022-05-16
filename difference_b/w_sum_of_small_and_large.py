s=str(input())
d=s.split()
t1=[]
t2=[]
for i in range(0,len(d)):
   c=min(d[i])
   t1.append(c)
   e=max(d[i])
   t2.append(e)
sum1=0
sum2=0
for i in range(0,len(t1)):
   sum1+=ord(t1[i])
for i in range(0,len(t2)):
   sum2+=ord(t2[i])
print(sum2-sum1)
   

