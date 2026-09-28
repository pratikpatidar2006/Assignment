"""
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found

---
"""

n=int(input("Enter size of list :"))
list=[]
print("Enter the elements of array")
for i in range(n):
     list.append(int(input()))
for i in range(n):
     count=0
     for j in range(n):
         if list[i]==list[j]:
             count+=1
     if count>n/2:
          print("Majority element found",list[i])
          break
else:
    print("No majority element found ")