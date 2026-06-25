"""
Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3
"""
#by while loop:-
"""
num=int(input("enter number: "))
count=0
while num>0:
    temp=num%10
    if temp%2==1:
        count+=1
    num=num//10
print(count)
"""
#by for loop:-

num=int(input("enter number: "))
count=0
for i in range(0,len(str(num))):
    temp=num%10
    if temp%2==1:
        count+=1
    num=num//10
print(count)



