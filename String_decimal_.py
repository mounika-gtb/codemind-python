t=int(input())
p="1234567890"
for i in range(0,t):
    op=0
    s=str(input())
    l=list(s)
    for i in range(0,len(l)):
        if l[i] not in p:
            op=1
            break
    #print(s)
    if op==1:
        print("False")
    if op==0:
        print("True")

            
        