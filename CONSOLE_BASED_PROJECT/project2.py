print()
str="""     =========================================
           BUS ROUTE MANAGEMENT SYSTEM
     ========================================="""

print(str)
print()
while True:
   print("1. View Available Routes")
   print("2. Check Bus Schedule")
   print("3. Check Bus Fare")
   print("4. Book Ticket")
   print("5. Exit")
   choice=int(input("Enter your choice:"))
   while choice ==1:
        str="""=========================================
                 View Available Routes
               =========================================

        1. Indore → Bhopal
        2. Indore → Ujjain
        3. Bhopal → Jabalpur
        4. Bhopal → Sagar
        5. Ujjain → Dewas
        6. Dewas → Indore

        """
        print(str)
        break

   while choice==2:
        print()
        print("      CHECK BUS SCHEDULE      ")
        print("==============================") 
        print("1. Indore")
        print("2. Ujjain")
        print("3. Bhopal")
        print("4. Dewas")
        print("5. Jabalpur")
        print("6. Sagar")
        src=int(input("Enter source : "))
        des=int(input("Enter destination :"))
        if src==1 and des==3:
             str="""---------------------------------
                      Route : Indore - Bhopal

                         Available Buses

               Bus Name         Departure     Arrival
              -----------------------------------------
               Express-101      06:00 AM      07:15 AM
               Shiv Express     09:30 AM      10:45 AM
               City Rider       02:00 PM      03:20 PM
               Night Express    07:00 PM      08:20 PM
              ---------------------------------"""
        elif src==1 and des==2:
             str="""---------------------------------
                      Route : Indore - Ujjain

                         Available Buses

               Bus Name         Departure     Arrival
              -----------------------------------------
               Satyam           06:00 AM      07:15 AM
               PatelTravels     09:30 AM      10:45 AM
               SherShah         01:00 PM      02:20 PM
               ShivShakti       07:00 PM      08:30 PM
              ---------------------------------"""
             print(str)

        elif src==3 and des==5:
             str="""---------------------------------
                      Route : Bhopal - Jabalpur

                         Available Buses

               Bus Name         Departure     Arrival
              -----------------------------------------
               Express-101      05:00 AM      06:15 AM
               Shivshankar      09:30 AM      10:55 AM
               CityExpess       02:00 PM      03:10 PM
               Satyasai         06:00 PM      07:50 PM
              ---------------------------------"""
             print(str)

        elif src==3 and des==6:
             str="""---------------------------------
                      Route : Bhopal - Sagar

                         Available Buses

               Bus Name         Departure     Arrival
              -----------------------------------------
               Express-101      06:00 AM      07:15 AM
               Shiv Express     09:30 AM      10:45 AM
               City Rider       02:00 PM      03:20 PM
               Night Express    07:00 PM      08:20 PM
              ---------------------------------"""
             print(str)

        elif src==2 and des==4:
             str="""---------------------------------
                      Route : Ujjain - Dewas

                         Available Buses

               Bus Name         Departure     Arrival
              -----------------------------------------
               Express-101      06:00 AM      07:15 AM
               Shiv Express     09:30 AM      10:45 AM
               City Rider       02:00 PM      03:20 PM
               Night Express    07:00 PM      08:20 PM
              ---------------------------------"""
             print(str)

        elif src==4 and des==1:
             str="""---------------------------------
                      Route : Dewas - Indore

                         Available Buses

               Bus Name         Departure     Arrival
              -----------------------------------------
               Express-101      06:00 AM      07:15 AM
               Shiv Express     09:30 AM      10:45 AM
               City Rider       02:00 PM      03:20 PM
               Night Express    07:00 PM      08:20 PM
              ---------------------------------"""
             print(str)

        else:
            print("oops ! No available buses  ")
        break
   while choice==3: 
        print("        CHECK FARE          ")
        print("............................")
        str="""
        1. Indore - Bhopal
        2. Indore - Ujjain
        3. Bhopal - Jabalpur
        4. Bhopal - Sagar
        5. Ujjain - Dewas
        6. Dewas  - Indore

            """
        print(str)
        print()
        route=int(input("Enter your route :"))
        if route==1:
            km=210
            print("Route   :  Indore - Bhopal")
            print()
            print("Original fare :",km*3)
            age=int(input("enter your age :"))
            if age>=65:
                print("Senior citizen discount :30%")
                print("Final Fare :",km*3*2/3)
            else:
                print("Final Fare :",km*3)

        elif route==2:
            km=85
            print("Route   :  Indore - Ujjain")
            print()
            print("Original fare :",km*3)
            age=int(input("enter your age :"))
            if age>=65:
                print("Senior citizen discount :30%")
                print("Final Fare :",km*3*2/3)
            else:
                print("Final Fare :",km*3)

        elif route==3:
            km=210
            print("Route   : Bhopal - Jabalpur")
            print()
            print("Original fare :",km*3)
            age=int(input("enter your age :"))
            if age>=65:
                print("Senior citizen discount :30%")
                print("Final Fare :",km*3*2/3)
            else:
                print("Final Fare :",km*3)

        elif route==4:
            km=140
            print("Route   : Bhopal - Sagar")
            print()
            print("Original fare :",km*3)
            age=int(input("enter your age :"))
            if age>=65:
                print("Senior citizen discount :30%")
                print("Final Fare :",km*3*2/3)
            else:
                print("Final Fare :",km*3)
        elif route==5:
            km=35
            print("Route   :  Ujjain - Dewas")
            print()
            print("Original fare :",km*3)
            age=int(input("enter your age :"))
            if age>=65:
                print("Senior citizen discount :30%")
                print("Final Fare :",km*3*2/3)
            else:
                print("Final Fare :",km*3)
        elif route==6:
            km=45
            print("Route   :  Dewas - Indore")
            print()
            print("Original fare :",km*3)
            age=int(input("enter your age :"))
            if age>=65:
                print("Senior citizen discount :30%")
                print("Final Fare :",km*3*2/3)
            else:
                print("Final Fare :",km*3)
        break
