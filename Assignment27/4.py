"""

4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

"""

while True:
         print()
         print("""1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit
""")
         x=int(input("Enter your choice :"))
         if x==4:
            break
         match(x):        
          case 1:
                
            r1=int(input("Enter the row of matrix 1 :"))
            c1=int(input("Enter the col of matrix 1 :"))
            A=[]
            print("Enter element of A :")
            for i in range(r1):
              row=[]
              for j in range(c1):
                 row.append(int(input()))
              A.append(row)
            sum1=0
            print("Main Diagonal Elements :",end=" ")
            for i in range(r1):
                   j=i
                   if i==j:
                       print(A[i][j],end=" ")
            sum1+=A[i][j]
               

                     
                                                
          case 2:
                  r1=int(input("Enter the row of matrix 1 :"))
                  c1=int(input("Enter the col of matrix 1 :"))
                  A=[]
                  print("Enter element of A :")
                  for i in range(r1):
                     row=[]
                     for j in range(c1):
                        row.append(int(input()))
                     A.append(row)

                  sum2=0
                  print("Secondry Diagonal Elements :",end=" ")
                  for i in range(r1):
                     for j in range(c1):
                        if i+j==r1-1:
                           print(A[i][j],end=" ")
                  sum2+=A[i][j]                                         
          case 3:
                print("Main Diagonal Sum =",sum1)
                print("Secondry Diagonal Sum =",sum2)
                if sum1==sum2:
                    print("Equal")
                else:
                    print("Not Equal")
                                  