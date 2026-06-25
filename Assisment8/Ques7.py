"""
Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3
"""
#by while loop:-
"""
num=int(input("enter number: "))
count=0
while num>0:
    temp=num%10
    if temp%2==0:
        count+=1
    num=num//10
print(count)
"""
#by for loop:-

num=int(input("enter number: "))
count=0
for i in range(1,len(str(num))):
    temp=num%10
    if temp%2==0:
        count+=1
    num=num//10
print(count)
