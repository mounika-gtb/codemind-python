s=str(input())
v="aeiou"
v1=0
num="1234567890"
d=0
cn=0
g=0
for i in range(0,len(s)):
    if s[i] in v:
        v1+=1
        
    elif s[i] in num:
        d+=1
    elif s[i]==" ":
        g+=1
    else:
        cn+=1
print("Vowels:",v1)
print("Consonants:",cn)
print("Digits:",d)
print("White spaces:",g)
        