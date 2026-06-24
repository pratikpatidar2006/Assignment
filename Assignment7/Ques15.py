"""
Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
"""

vehicle=input("Enter vehicle type: ")
hours=int(input("Enter hours parked: "))


if vehicle=="Bike":
   fee=hour*10
elif vehicle=="Car":
   fee=hours*20
else:
   fee=hours*50
if hours>5:
   fee=fee+100
print("Total Parking Fee: ",fee)
    
   
