"""
Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan
"""

data=float(input("Enter daily data usage in GB: "))
if data>3:
    print("Premium Plan")
elif data>1:
    print("Standard Plan")
else:
    print("Basic Plan")