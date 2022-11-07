s=input()
d=s[:2]

if s[len(s)-2:]=="AM":
    if int(d)==12:
        print("00"+s[2:len(s)-3])
    else:
        print(s[:len(s)-3])
else:
    if int(d)==12:
        print(s[:len(s)-3])
    else:
        d=int(d)+12
        print(str(d)+s[2:len(s)-3])