"""
1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found

---
"""

n=int(input("Enter the length of list : "))
list=[]
visited=[]
for i in range(n): 
     x=int(input("enter list element :"))
     list.append(x)
for i in range(n):
    if list[i] not in visited:
        visited.append(list[i])
        count=0
        for j in range(i+1,n):
               if list[i]==list[j]:
                      count+=1
        if count==0:
                print("First non-repeating number =",list[i])
                break
else:
     print("No non-repeated value found")
 