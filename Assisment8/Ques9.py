"""
Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
"""
#by while loop:-
"""
num=int(input("enter number: "))
flag="Even"
while num>0:
    x=num%10
    if x%2==1:
        flag="Not Even"
    num=num//10
print(flag)
"""
#by for loop:-
num=int(input("enter number: "))
flag="Even"
for i in range(1,len(str(num))):
    x=num%10
    if x%2==1:
        flag="Not Even"
    num=num//10
print(flag)