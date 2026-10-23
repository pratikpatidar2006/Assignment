"""
2.
 Employee Bonus Calculation (Using filter() and map() with Lambda Expressions)


A software company wants to reward its high-performing employees with a 10% bonus. However, only employees earning ₹50,000 or more are eligible for
 the bonus.

As a software developer, your task is to:

Filter the salaries of eligible employees.
Calculate the updated salary after adding a 10% bonus.
Display the final salaries of the eligible employees.

Note: Use filter() to identify eligible employees and map() to calculate the updated salaries. Both operations must use lambda expressions.

Input Format
The first line contains an integer N, representing the number of employees.
The second line contains N space-separated salary values.
Output Format

Display the updated salaries of all eligible employees after adding a 10% bonus.

Sample Input
Enter the number of employees:
6

Enter the salaries:
35000 50000 62000 45000 70000 55000
Sample Output
Eligible Employees' Updated Salaries:
55000.0 68200.0 77000.0 60500.0

"""

x=int(input("Enter number of employees:"))
salaries=list(map(int, input("Enter the salaries: ").split()))

updated_salaries = map(lambda x: int(x * 1.10),salaries)
final_salaries = list(updated_salaries)
print("Final salaries of eligible employees (with 10% bonus):", final_salaries)