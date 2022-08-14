n=int(input())
a=input()
b=a.split()
for i in range(0,len(b)):
    c=b.count(b[i])
    if c==1:
        print(b[i])
        break