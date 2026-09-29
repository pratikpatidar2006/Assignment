"""

3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45

"""
print("""1.Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
""")

x=int(input("Enter choice :"))
match(x):
    case 1:
        r=int(input("how many employees:"))
        c=int(input("how many months :"))
        matrix=[]
        for i in range(r):
           row=[]
           for j in range(c):
              row.append(int(input()))
           matrix.append(row)
        max=0
        for i in range(r):
             sum=0
             for j in range(c):
                 sum=sum+matrix[i][j]
                 
             if sum>max:
                 max=sum
                 x=i
        print("Employee ",x+1,"Highest total score =",max)
               

    case 2:
        r=int(input("how many employees:"))
        c=int(input("how many months :"))
        matrix=[]
        for i in range(r):
           row=[]
           for j in range(c):
              row.append(int(input()))
           matrix.append(row)
        mini=[]
        for i in range(r):
             sum=0
             for j in range(c):
                 sum=sum+matrix[j][i]
             avg=sum/r
             mini.append(int(avg))       
             
        print("Month ",min(avg))
               