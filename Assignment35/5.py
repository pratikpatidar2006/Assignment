"""

QNO:
Employee Data Processing System

A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function and variable names and follow proper indentation

"""
age=list(map(int,input("Enter the age of employees :").split()))
name=input("Enter the name :")

def second_high(age):
       updated=list(sorted(age,reverse=True))
       return updated[1]

def senior_employees(age):
        senior=list(filter(lambda x:x>50,age))
        return count(senior)

def unique(age):
       diffrent=set(age)
       return list(diffrent) 

def vowel(name):
     name_list = name.split()
     vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
     vowel_names = list(filter(lambda name: name.startswith(vowels), name_list))
     return len(vowel_names)

def longest(name):
     name_list=name.split()
     if not name_list:
        return ""
     else:
       return max(name_list, key=len)




while True:
     print()
     print("""Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================""")
     print()

     c=int(input("Enter your choice :"))
     match(c):
         case 1:
             print("Second highest age :",second_high(age))

         case 2:
             print("Count of senior is :",senior_employees(age))
         
         case 3:
             print("Unique age :",unique(age))
        
         case 4:
             print(vowel(name))
             
         case 5:
             print(longest(name))

         case 6:
             break