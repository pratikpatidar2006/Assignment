"""
2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System
"""

while True:
        print()
        print("""enter your Choice
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit""")
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
                   count=0
                   for j in range(c1):
                       prime=True
                       for x in range(2,(A[i][j]//2)+1):
                           if A[i][j]%x==0:
                               prime=False
                       if prime==True and A[i][j]>1:
                            count+=1
                        
                   print("row ",i,"prime count ",count)
               
           case 2:
              for i in range(r1):
                   count=0
                   for j in range(c1):
                      x=1
                      sum=0
                      while x<=A[j][i]//2:
                            if A[j][i]%x==0:
                                sum+=x
                            x+=1
                      if sum==A[j][i]:
                         count+=1 
                   print("Perfect number count of column" ,i,"=",count) 
                         
           case 3:
               for i in range(r1):
                   sum=0
                   for j in range(c1):
                      sum+=A[i][j]
                   print("Sum of Row ",i,"=",sum)                                  
