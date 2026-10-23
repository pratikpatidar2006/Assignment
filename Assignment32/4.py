"""
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

---

"""

d={}
n=int(input("Enter number of stiudents :"))
for i in range(n):
    name=input("Enter name :")
    marks=int(input("Entr marks :"))
    d[name]=marks



highest = max(d, key=d.get)
lowest = min(d, key=d.get)

print("Highest Marks :", highest, d[highest])
print("Lowest Marks :", lowest, d[lowest])



"""
for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

    if marks < lowest_marks:
        lowest_marks = marks
        lowest_name = name

print("Highest Marks :", highest_name, highest_marks)
print("Lowest Marks :", lowest_name, lowest_marks)

"""