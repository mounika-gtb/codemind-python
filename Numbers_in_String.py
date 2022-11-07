s=input()
p="1234567890"
cnt=0
for i in range(0,len(s)):
    if s[i] in p:
        cnt+=int(s[i])
print(cnt)