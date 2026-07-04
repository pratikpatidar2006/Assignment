"""WAP to find out the sum of all integer between 100 and 200 which are divisible by 9"""

a=int(input("enter first number: "))
b=int(input("enter second number: "))
i=a
sum=0
while i<=b:
   if i%9==0:
      sum=sum+i
   i=i+1
print("Sum: ",sum)

      