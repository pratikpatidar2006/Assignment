age=int(input("Enter age: "))
weight=int(input("enter Weight: "))
goal =input("Enter goal: ")

if age>=18:
    if weight>=80:
       if goal.lower()=="weight loss":
          print("Plan = Cardio Plan")
       else:
          print("Plan  = Strength plan")
    else:
       print("Plan = General Fitness Plan ")
else:
    print("Not allowed")
     