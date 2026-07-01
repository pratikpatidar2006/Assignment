"""
Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU
"""

age=int(input("Age: "))
sever=input("Severity: ")
insure=input("Insurance: ")

if sever=="critical":
   if age>=60:
      print("Immediate ICU")
   else:
      print("Emergency Ward")
elif sever=="moderate":
   if insure=="yes":
      print("Priority Treatment")
   else:
      print("General Queue")
else:
   if sever=="low":
      if age<10:
         print("Pediatric Priority")