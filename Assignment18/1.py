"""
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8


#without function 

n=input("Enter feedback message:")
count=0
for ch in n :
    if ch=="i" or ch=="a" or ch=="o" or ch=="u" or ch=="e" or ch=="I" or ch=="A" or ch=="O" or ch=="U" or ch=="E":
             count+=1
             
print("Total vowels :",count )

"""

# without function

ch=input("Enter feedback message:")
count=0
for i in ch:
     if i in "aeiou":
       count+=1
print("Total vowels :",count)



