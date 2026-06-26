"""
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12
"""
n =int(input("Enter number"))
i=1
sum=0
while n>=i*i:
       d=n//i
       sum=sum+d+i
       i+=1
print(sum)       

       

