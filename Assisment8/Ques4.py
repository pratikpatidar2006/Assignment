"""
Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321
"""
#by while loop:-
"""
num=int(input("Enter Number: "))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)
"""
#by for loop:-

num=int(input("Enter Number: "))
rev=0
for i in range(0,len(str(num))):
    rev=rev*10+num%10
    num=num//10
print(rev)
   
