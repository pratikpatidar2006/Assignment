"""
Number Range Display System (if-elif with loops)*
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using *if-elif-else and loops* to implement this logic.
"""

n1,n2=map(int,input("Enter two number: ").split(" "))
if n1<n2:
    for i in range(n1,n2+1):
        print(i,end=" ")
elif n1>n2:
    for i in range(n1,n2,-1):
        print(i,end=" ")
else:
    print("Both number are Same")