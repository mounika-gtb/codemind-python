n=int(input())
cnt=0
for i in range(0,n):
    s=str(input())
    #print(s)
    if s=="X++":
        cnt+=1
        #print(s,cnt)
    if s=="++X":
        cnt+=1
        #print(s)
    if s=="X--" or s=="--X":
        cnt-=1
        #print(s,cnt)
print(cnt)

    