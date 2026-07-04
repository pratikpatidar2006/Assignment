"""Reverse Number Triangle Pattern"""

n=int(input("enter n: "))
i=1
while i<=n:
   print()
   s=1
   while s<=i:
      print(" ",end=" ")
      s=s+1
   j=n
   while j>=i:
      print(j,end=" ")
      j=j-1
   i=i+1
  
   