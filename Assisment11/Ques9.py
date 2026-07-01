"""
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
"""

n=int(input("Enter Number: "))
rev=0
sum=0
max=0
temp=n
for i in range(len(str(n))):
   rev=rev*10+n%10
   n=n//10
print(rev)
n=temp
while n>9:
   a=n%10
   n=n//10
   b=n%10
   d=abs(a-b)
   sum=sum+d
   if d>=max:
      max=d
   print(d,end=" ")
print("\n",sum)
print(max)
if sum%len(str(temp))==0:
   print("Balance")
else:
   print("Unbalance")

   

   
   