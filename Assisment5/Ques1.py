age=int(input("enter age: "))
if age>=18:
    id=input("if proof is available (yes/no): ")
    if id.lower()=="yes":
          print("allowed inside Booth")
          print("You are eligible to vote")
    else:
          print("You have not id ")
else:
     print("Your age is less than 18")