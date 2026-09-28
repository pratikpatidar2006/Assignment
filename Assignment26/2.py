"""
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 5

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

---
"""

n=int(input("Enter the length of list : "))
list=[]
for i in range(n): 
     x=int(input("enter list element :"))
     list.append(x)
for i in range(n):
        count=0
        for j in range(i+1,n):
               if list[i]==list[j]:
                      count+=1
        if count==1:
                print("First repeating number =",list[i])
                break
else:
     print("No repeated value found")
 