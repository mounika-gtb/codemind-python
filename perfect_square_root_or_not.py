n=int(input())
for i in range(1,n):
   c=i*i
   if c==n:
      print("True")
      break
   elif i>n//2:
      print("False")
      break


