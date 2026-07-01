"""
7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime

"""
import math
n=int(input("Enter Number:"))
sum=0
while n:
     mod=n%10
     n=n//100
     sum=sum+mod
print("Sum is ",sum)
if sum<=1:
    print("Not prime")
else:
    i=2
    while i<=math.sqrt(sum):
         if sum%i==0:
              print("Not a Prime Number")
              break
         i+=1
    else:
        print("Sum is Prime ")

    
           
