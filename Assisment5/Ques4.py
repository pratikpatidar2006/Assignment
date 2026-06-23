age=int(input("Enter age"))
BMI=int(input("Enter BMI"))

if age>=18:
    print("GYM access Granted")
    if BMI>25:
         print("Enroll in weight Loss program")
    else:
         print("Allowed for GYM")
else:
   print("GYM access Denied")