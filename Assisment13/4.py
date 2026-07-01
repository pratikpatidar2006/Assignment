"""4.Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code
"""

x=True
n=int(input("Enter number:"))
for i in range(1,len(str(n))):
         for j in range(i+1,len(str(n))):
                   if i==j:
                      print("Invalid Code")
                      break
else:
    print("Valid Code")
         
            

     