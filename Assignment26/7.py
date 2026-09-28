"""
7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

---
"""
n=int(input("Enter size of array :"))
k=int(input("How much element rotate :"))
list=[]
list1=[]
for i in range(n):
      x=int(input("Enter value "))
      list.append(x)
for i in range(n-k,n):
      list1.append(list[i])
for i in range(n-1,k-1,-1):
     list[i]=list[i-k] 
print(list1)
for i in range(k):
      list[i]=list1[i]
print(list)
