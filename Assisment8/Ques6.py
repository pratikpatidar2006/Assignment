"""
Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
"""
#by while loop:-
"""
num=int(input("Enter number: "))
sum=0
temp=num
while num>0:
    x=num%10
    sum=sum+x*x*x
    num=num//10
if sum==temp:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
"""
#by for loop:-

num=int(input("Enter number: "))
sum=0
temp=num
for i in range(0,len(str(num))):
    x=num%10
    sum=sum+x*x*x
    num=num//10
if sum==temp:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")

