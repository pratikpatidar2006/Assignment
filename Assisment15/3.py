"""
3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
"""
import math
a=int(input("Enter number first  :"))
b=int(input("Enter number second  :"))
while a<=b:
     l=int(math.sqrt(a))
     for i in range(2,l+1):
         if a%i==0:
             break
     else:
        print(a)
     a+=1
         
  
             


