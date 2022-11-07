s=str(input())
p="1234567890"
cnt=0
for i in range(0,len(s)):
    if s[i] in p:
        cnt+=1
if cnt!=0:
    print("Contains",cnt,"digit")
else:
    print("Doesn't contain digit")