s=input()
a=s[:2]
if int(a)==0:
    print("12:00 AM")

elif int(a)<12:
    print(s+" "+"AM")
elif int(a)==12:
    print(s+" "+"PM")
else:
    d=abs(12-int(a))
    if d<10:
        print("0"+str(d)+s[2:]+" "+"PM")
    else:
        print(str(d)+s[2:]+" "+"PM")
    