t=int(input())
p="1234567890"
for i in range(0,t):
    s=str(input())
    op=0
    for i in range(0,len(s)):
        if s[i] in p: 
            op=1
            break
    if op==0:
        print("No")
    else:
        print("Yes")