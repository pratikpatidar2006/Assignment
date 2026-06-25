"""
Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
"""
#by while loop:-
"""
num=int(input("Number: "))
digit=int(input("Digit: "))
count=0
while num>0:
    if digit==num%10:
        count+=1
    num=num//10
print(count)
"""
#by while loop:-
num=int(input("Number: "))
digit=int(input("Digit: "))
count=0
for i in range(0,len(str(num))):
    if digit==num%10:
        count+=1
    num=num//10
print(count)

