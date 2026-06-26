"""
Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9
"""
num=int(input("enter the number: "))
max=0
while n:
    d=num%10
    if(d>=max):
    max=d
    num=num//10
print("Largest Digit: ",max)
