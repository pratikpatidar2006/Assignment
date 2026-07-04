"""Left-Aligned Half Pyramid Star Pattern"""

n=int(input("enter n: "))
i=1
while i<=n:
   print()
   s=1
   while s<=n-i:
      print(" ",end=" ")
      s=s+1
   p=1
   while p<=i:
      print("*",end=" ")
      p=p+1
   i=i+1