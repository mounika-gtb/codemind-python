n=int(input())
l=list(map(int,input().split()))
l1=list(set(l))
for i in range(0,len(l1)):
    if l.count(l1[i])>n/2:
        print(l1[i])