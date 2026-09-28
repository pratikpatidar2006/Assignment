"""
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

---
"""

n=int(input("Enter size of list :"))
list=[]
print("Enter the elements of array")
for i in range(n):
     list.append(int(input()))
for i in range(n):
    sum=0
    sum1=0
    for j in range(0,i):
          sum+=list[j]
    
    for k in range(i+1,n):
          sum1+=list[k]
    
    if sum==sum1:
        print("Equilibrium Index found ",i)
        break
else:
    print("No equilibrium character found ")