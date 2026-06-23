"""
A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
"""
unit1=int(input("Unit1: "))
unit2=int(input("Unit2: "))
unit3=int(input("Unit3: "))
unit4=int(input("Unit4: "))
unit5=int(input("Unit5: "))
unit6=int(input("Unit6: "))

if unit1>unit2:
    if unit1>unit3:
        if unit1>unit4:
            if unit1>unit5:
                if unit1>unit6:
                    print("Unit1 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
            else:
                if unit5>unit6:
                    print("Unit5 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
        else:
            if unit4>unit5:
                if unit4>unit6:
                    print("Unit4 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
            else:
                if unit5>unit6:
                    print("Unit5 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
    else:
        if unit3>unit4:
            if unit3>unit5:
                if unit3>unit6:
                    print("Unit3 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
            else:
                if unit5>unit6:
                    print("Unit5 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
        else:
            if unit4>unit5:
                if unit4>unit6:
                    print("Unit4 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
            else:
                if unit5>unit6:
                    print("Unit5 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
else:
    if unit2>unit3:
        if unit2>unit4:
            if unit2>unit5:
                if unit2>unit6:
                    print("Unit2 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value") 
            else:
                if unit5>unit6:
                    print("Unit5 has Highest Stock Value")
                else:
                    print("Unit6 has Highest Stock Value")
        else:
           if unit4>unit5:
               if unit4>unit6:
                   print("Unit4 has Highest Stock Value")
               else:
                   print("Unit6 has Highest Stock Value")
           else:
               if unit5>unit6:
                    print("Unit5 has Highest Stock Value")
               else:
                    print("Unit6 has Highest Stock Value")
    else:
        print("Unit3 has Highest Stock Value")

