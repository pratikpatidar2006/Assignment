"""
7.

=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi

---

"""
d={}
n=int(input("Enter number :"))

for i in range(n):
     key=input("Enter key :")
     value=int(input("Enter value :"))
     d[key]=value
     
for k,v in d.items():
    if v>30:
        print(k,":",v )
     