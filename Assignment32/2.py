"""

2.

=========================================
EMPLOYEE DEPARTMENT COUNT
=========================

A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.

Sample Output:
{'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}

---

"""

emp=[]
n=int(input("enter employees strength :"))
d={}
for i in range(n):
    values=input("Enter values :")
    emp.append(values)
for user in emp:
     d[user]=d.get(user,0)+1
print(d)