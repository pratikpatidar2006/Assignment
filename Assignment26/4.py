"""
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

---
"""
n=int(input("Enter length :"))
arr=[]
for i in range(n):
     x=int(input("Enter value :"))
     arr.append(x)
max=0
for i in range(n):
     n=1
     while n<=arr[i]:
         if arr[i]-n in arr:
            n+=1
         else:
            break
     if max<n:
          max=n    
print(max)