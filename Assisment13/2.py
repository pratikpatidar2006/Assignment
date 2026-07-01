"""2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime
"""
import math
n=int(input("Enter number :"))
sum=0
prod=1
count=0
while n:
    mod=n%10
    sum=sum+mod
    prod=prod*mod
    n=n//10
print("Product is ",prod)
print("Sum is ",sum)
diff=abs(prod-sum)
print("Diffrence is ",diff)
temp=diff
while diff:
       count+=1
       diff=diff//10           
final=temp+count
print("Final Result ",final)
if final<=1:
     print("Not a prime number")
else:
     i=2
     while i<=math.sqrt(final):
          if final%i==0:
              print("Not a Prime")
              break
          i+=1
     else:
         print("Prime Number")          