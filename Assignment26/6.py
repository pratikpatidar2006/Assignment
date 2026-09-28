"""
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]

---
"""

n=int(input("Enter size :"))
list=[]
product=[]
print("Enter element of arraY")
for i in range(n):
     list.append(int(input()))
     
for i in range(n):
    prod=1
    for j in range(n):
         if i==j:
             pass
         else:
            prod*=list[j] 
    product.append(prod)
print("Output :",product)