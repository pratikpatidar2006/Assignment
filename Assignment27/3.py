"""

3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2
"""


while True:
        print()
        print("""1.Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit
""")
        x=int(input("Enter your choice :"))
        if x==4:
            break
        r1=int(input("Enter the row of matrix 1 :"))
        c1=int(input("Enter the col of matrix 1 :"))
        A=[]
        print("Enter element of A :")
        for i in range(r1):
           row=[]
           for j in range(c1):
               row.append(int(input()))
           A.append(row)

        
        match(x):
           case 1:
              for i in range(r1):
                    countarm=0
                    for j in range(c1):
                       x=A[i][j] 
                       count=0
                       while x:
                           x=x//10
                           count+=1
                       sum=0
                       a=A[i][j]
                       for x in range(count):
                           sum+=(A[i][j]%10)**count
                           A[i][j]=A[i][j]//10
                       
                       if sum==a:
                           countarm+=1
                    print("Row ",i,"Armstrong Count =",countarm)
                                                
           case 2:
              for i in range(r1):
                    countpalindrome=0
                    for j in range(c1):
                       x=A[j][i] 
                       count=0
                       while x:
                           x=x//10
                           count+=1
                       sum=0
                       a=A[j][i]
                       for x in range(count):
                           sum=(A[j][i]%10)+sum*10
                           A[j][i]=A[j][i]//10
                       
                       if a==sum:
                           countpalindrome+=1
                    print("Row ",i,"Palindrome count =",countpalindrome)


                         
           case 3:
               for i in range(r1):
                   sum=0
                   for j in range(c1):
                      sum+=A[i][j]
                   print("Average of Row ",i,"=",sum/c1)                                  
