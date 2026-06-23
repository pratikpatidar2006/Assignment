age=int(input("Enter age : "))
show_time=input("monring/evening : ")
day_type=input("weekday/weekend : ")

if age<18:
    if show_time.lower()=="morning":
         print("Ticket price = 100")
    else:
         print("Ticket Price = 150")
else:
    if show_time.lower()=="evening":
         if day_type=="weekend":
             print("Ticket Price =300")
         else:
             print("Ticket price = 250")
    else:
         printr("Ticket Price = 200")