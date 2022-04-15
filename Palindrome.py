n=int(input())
z=n
sum=0
while n:
    r=n%10
    sum=sum*10+r
    n=n//10
if sum==z:
    print("True")
else:
    print("False")