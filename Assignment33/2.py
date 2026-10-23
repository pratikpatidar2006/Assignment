"""
2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System"""
students = {}

while True:
  print("\n=========================================")
  print("student managemnt system")
  print("=========================================")
  print("1. Add new student")
  print("2. Search student")
  print("3. Update course")
  print("4. Delete student")
  print("5. Display all students")
  print("6. Count total students")
  print("7. Display students by course")
  print("8. Display students by city")
  print("9. Find student paying highest fees")
  print("10. find student paying lowest fees")
  print("11. Exit")

  choice = int(input("Enter your choice : "))

  if choice == 1:
    student_id = int(input("Enter student id : "))

    if student_id in students:
      print("student id already exists")
    else:
      name = input("Enter Student name : ") 
      course = input("Enter course name : ") 
      mobile = input("Enter mobile number : ")
      fees = int(input("Enter fees : "))
      city = input("Enter city : ")
      students[student_id] = {
        "name" : name,
        "course" : course,
        "mobile" : mobile,
        "fees" : fees,
        "city" : city
      }
      print("student added successfully")

  if choice == 2:
    student_id = int(input("Enter student id to search :"))
    if student_id in students:
      print("student id :", student_id)
      print("Name       :", students[student_id]["name"])
      print("Course     :", students[student_id]["course"])
      print("Mobile     :", students[student_id]["mobile"])
      print("Fees       :", students[student_id]["fees"])
      print("City       :", students[student_id]["city"])

  if choice == 3:
    student_id = int(input("Enter student id to update course : "))
    
    if student_id in students:
       new_course = input("Enter New Course: ")
       students[student_id]["course"] = new_course
       print("Course Update Successfully")
    else:
       print("Student ID Not Found")

  if choice == 4:
    student_id = int(input("Enter student id to delete: "))
    
    if student_id in students:
       del students[student_id]
       print("Student id delete successfully")
    else:
       print("Student id not found")

  if choice == 5:
    for student_id in students:
      print("-----------------------------------")
      print("students id :", student_id)
      print("NAME        :", students[student_id]["name"])
      print("COURSE      :", students[student_id]["course"])
      print("FEES        :", students[student_id]["fees"])
      print("CITY        :", students[student_id]["city"])
      print("-----------------------------------")

  if choice == 6:
    print("Total Students :", len(students))

  if choice == 7:
    course = input("Enter course name : ")
    found = False
    for student_id, details in students.items():
      if details["course"].lower() == course.lower():
        print(student_id, ":", details["name"])
        found = True
    if not found:
      print("No Students Found")

  if choice == 8:
    city = input("Enter city name : ")
    found = False
    for student_id, details in students.items():
      if details["city"].lower() == city.lower():
        print(student_id, ":", details["name"])
        found = True
    if not found:
      print("No students found")

  if choice == 9:

    highest_fees = 0
    highest_id = None

    for student_id, details in students.items():

        if highest_fees < details["fees"]:
            highest_fees = details["fees"]
            highest_id = student_id

    print("Highest Fees:", highest_fees)
    print("Student ID:", highest_id)

  if choice == 10:
      
      lowest_fees = 100
      lowest_id = None

      for student_id, details in students.items():

        if lowest_fees > details["fees"]:
            lowest_fees = details["fees"]
            lowest_id = student_id

      print("lowest Fees:", lowest_fees)
      print("Student ID:", lowest_id)
  
  if choice == 11:
      print("Thank You For Using Student Management System")


