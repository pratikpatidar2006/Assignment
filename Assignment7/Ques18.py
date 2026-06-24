"""
Smart Loan Risk Categorization

A bank categorizes loan applicants into risk levels based on salary, credit score, and number of existing loans.

If salary is at least 30000, then check credit score. If credit score is 750 or above, then check number of loans. If zero, assign low risk. If loans are up to 2, assign medium risk; otherwise high risk. If credit score is below 750, then check if salary is at least 50000. If yes, check if credit score is at least 650. If yes, medium risk; otherwise high risk. If salary is less than 30000, mark as not eligible.

Input:
Salary = 40000
Credit Score = 760
Existing Loans = 1
"""

salary=int(input("Salary = ")
if salary>=30000:
     credit=int(input("Credit Score = "))
     if credit>=750:
          loans=int(input("Existing Loans = "))
          if loans==0:
              print("Low Risk")
          elif loans<=2:
              print("Assign Risk")
          else:
              print("High Risk")
     else:
         if salary<=50000:
             if credit<=650:
                  print("Medium Risk")
             else:
                  print("High Risk") 
else:
     print("Mark as not eligible")
      
