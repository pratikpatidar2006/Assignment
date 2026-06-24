"""
Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
"""

amount=int(input("Enter bill amount: "))
if amount<=1000:
   gst=(5/100)*amount
elif amount<=5000:
   gst=(12/100)*amount
else:
   gst=(18/100)*amount
if amount<=8000:
   gst=gst+200
print("Final Bill Amount: ",amount+gst)
   
