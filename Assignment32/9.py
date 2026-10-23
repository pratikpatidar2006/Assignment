"""
9.

=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker

"""

stock={}
n=int(input("Number of items"))

for i in range(n):
    key=input("Enter key:")
    value=int(input("Enter value :"))
    stock[key]=value

for key,value in stock.items():
    if value<30:
       print(key)
