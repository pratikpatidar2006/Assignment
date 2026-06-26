n=int(input("Enter number"))

for i in range(len(str(n))):
      ans=n%10
      n=n//10
print("First Digit is :",ans)
     