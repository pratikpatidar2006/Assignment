"""

7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3

"""

n=int(input("Enter size of list:"))
list=[]
fact=[]
counteven=0
for i in range(n):
   x=int(input("Enter the value of array :"))
   list.append(x)

for i in list:
     x=1
     for j in range(1,i+1):
          x*=j
     fact.append(x) 
     if x%2==0:
         counteven+=1
print(fact)
print("Maximum :",max(fact))
print("Sum :",sum(fact))
print("Count :",counteven)

     
             
