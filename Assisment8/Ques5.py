"""
Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome
"""

#by while loop:-
"""
num=int(input("enter number: "))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)
"""
#by for loop:-

num=int(input("enter number: "))
rev=0
for i in range(0,len(str(num))):
    rev=rev*10+num%10
    num=num//10
print(rev)