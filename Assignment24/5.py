"""
---

4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]

"""

n=int(input("Enter size :"))
list=[]
for i in range(n):
      x=int(input("Enter number :"))
      list.append(x)
palindrome=[]
count=0
for i in range(len(list)):
     x=list[i]
     x1=0
     xx=x
     while x:
       x1=x1*10+x%10
       x=x//10
     if x1==xx:
         palindrome.append(x1)
         count+=1
print("Palimdrome number list :",palindrome)
print("Count :",count)
print("Max palindrome number :",max(palindrome))
print("Sorted  palindrome number :",sorted(palindrome))     
     
 