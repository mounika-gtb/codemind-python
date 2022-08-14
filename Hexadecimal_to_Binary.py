q=int(input())
for i in range(0,q):
    n=input()
    d=int(n,16)
    b=bin(d)[2:]
    c=((((len(b)//4)+1)*4))
    if len(b)%4!=0:
        print(b.zfill(c))
    else:
        print(b)
    