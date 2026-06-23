member=input("you are active(yes/no)")
book_issue=int(input("Enter no of issued of book"))

if member.lower()=="yes":
     print("Entry allowed")
     if book_issue<3:
         print("Can issue more Books")
else:
    print("Entry denied")