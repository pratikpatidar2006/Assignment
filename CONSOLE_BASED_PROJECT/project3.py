print()
s="""******** CHAR DHAM YATRA MANAGEMENT SYSTEM ********

1. Kedarnath
2. Badrinath
3. Gangotri
4. Yamunotri
5. Budget & Plans 
6. Exit
  """ 

while True:
    
   print(s)
   d=int(input("Select your Destination :"))
   match d:
           case 1:
                 str=""" ----Welcome to Kedarnath-----

1. Place Information
2. Hotel & Food Cost
3. Transport Cost
4. VIP Darshan
5. Pony / Palki / Helicopter
6. Total Budget Calculator
7. Things to Carry
8. Back"""       
                  
                 while True : 
                       print()   
                       print(str)
                       i=int(input("enter your enquiery : "))
                       print()
                       if i==1:
                           info="""
    ******** KEDARNATH ********

Location : Rudraprayag, Uttarakhand
Famous For : Lord Shiva Temple (Jyotirlinga)
Height : 3,583 m
Best Time : May–June, September–October
Trip Duration : 2–3 Days
Temple Open : May to October/November"""
                           print()
                           print(info)
                           print()
                           i=input("Any other enquiry (yes/no)").lower()
                           if i=="no":
                                print()
                                break
                       elif i==2:
                              print(" HOTEL")
                              print()
                              print("Budget = 1200/night")
                              print("Deluxe = 2500/night")
                              print("Luxury = 5000/night")
                              print()
                              print(" FOOD")
                              print()
                              print("Breakfast = 150/head")
                              print("Lunch     = 250/head")
                              print("Dinner    = 300/head")
                              print()
                              i=input("Any other enquiry (yes/no)").lower()
                              if i=="no":
                                     print()
                                     break
                       elif i==3:
                              print(" TRANSPORT ")
                              print("Bus = 2500")
                              print("Taxi = 4500")
                              print("Private Car = 7500")
                              i=input("Any other enquiry (yes/no)").lower()
                              if i=="no":
                                     print()
                                     break
                       elif i==4:
                              print("******VIP DARSHAN********")
                              print()
                              print("VIP Pass : ₹2100/person")
                              print()
                              print("Morning Darshan : 4:00 AM - 7:00 AM")
                              print("Morning Darshan : 6:00 PM - 8:00 PM")
                              print("Online Booking Available")
                              i=input("Any other enquiry (yes/no)").lower()
                              if i=="no":
                                     print()
                                     break
                       elif i==5:
                              print("******** SERVICES ********")
                              print()
                              print("Pony : ₹3500")
                              print("Palki : ₹5500")
                              print("Kandi : ₹4500")
                              print("Helicopter : ₹8500/person")
                              i=input("Any other enquiry (yes/no)").lower()
                              if i=="no":
                                     print()
                                     break
                       elif i==6:
                              print()
                              print("Make your Budget with us.....")
                              print()
                              day=int(input("stay duration in days :"))
                              print()
                              print("1. Bus")
                              print("2. Taxi")
                              print("3. Private Car")
                              trnp=int(input("Select mode of transport :"))

                              print()
                              print("1. Dharamshala")
                              print("2. Home Stay ")
                              print("3. Delux Hotel")
                              htl=int(input("select category of stay :"))

                              print()
                              print("1. Simple Thaali")
                              print("2. Diet Thaali")
                              print("3. Maharaja Thaali")
                              food=int(input("select food type :"))

                              print()
                              print("1. yes")
                              print("2. no")
                              vip=int(input("do you want VIP dharshan :"))

                              print()
                              print("1. Pony")
                              print("2. Palki ")
                              print("3. helicopter")
                              print("4. No need ")
                              service=int(input("select service :"))

                              print()
                              sum=0
                              match trnp:
                                 case 1:
                                       print("------Total Expenses-------")
                                       print()
                                       print(" Bus ₹ ",3500)
                                       sum=sum+3500
                                 case 2:        
                                       print("------Total Expenses-------")
                                       print()
                                       print(" Train+Taxi ₹ ",6000)
                                       sum=sum+6000
                                 case 3:
                                       print("------Total Expenses-------")
                                       print()
                                       print(" Private Car for 4 Person ₹ 9000")
                                       sum=sum+9000

                              match htl:
                                 case 1:
                                       print()
                                       print(" Camp/Dharmshala ₹ ",400*day)
                                       sum=sum+400*day
                                 case 2:
                                       print()
                                       print(" Home Stay ₹ ",1500*day)
                                       sum=sum+1500*day
                                 case 3:
                                       print()
                                       print(" Delux Hotel ₹ ",2500*day)
                                       sum=sum+1500*day
                              match food:
                                 case 1:
                                       print()
                                       print(" Simple Thaali ₹ ",300*day*2)
                                       sum=sum+300*day*2
                                 case 2:
                                       print()
                                       print(" Diet Thaali ₹ ",270*day*2)
                                       sum=sum+270*day
                                 case 3:
                                       print()
                                       print(" Maharaja Thaali ₹ ",650*day*2)
                                       sum=sum+650*day
                              match vip:
                                 case 1:
                                       print()
                                       print(" Vip Pass ₹2100")
                                       sum=sum+2100
                                 case 2:
                                       
                                       pass
                                       
                              match service:
                                 case 1:
                                       print()
                                       print(" Poni ₹ 3500")
                                       sum=sum+3500
                                 case 2:
                                       print()
                                       print(" Palki ₹ 5500")
                                       sum=sum+5500
                                 case 3:
                                       print()
                                       print(" Helicopter ₹ 8500")
                                       sum=sum+8500
                                 case 4:
                                       print(" Service ₹ 0")
                              print()
                              print("------------------------------")
                              print("Total Expenses : ₹",sum)
                              print()

                              extra=sum*0.20
                              print("Extra Expenses (20%) : ₹",extra)
                              print()

                              print("Final Budget : ₹",sum+extra)
                              print("------------------------------")
                              i=input("Any other enquiry (yes/no)").lower()
                              if i=="no":
                                     print()
                                     break
                       elif i==7:
                             
                                  print("****** THINGS TO CARRY ******")
                                  print()
                                  print("1. Aadhaar Card / ID Proof")
                                  print("2. Trekking Shoes")
                                  print("3. Warm Woollen Clothes")
                                  print("4. Raincoat / Umbrella")
                                  print("5. Torch & Extra Batteries")
                                  print("6. Water Bottle")
                                  print("7. Energy Bars / Dry Fruits")
                                  print("8. Personal Medicines")
                                  print("9. Power Bank")
                                  print("10. Backpack")
                                  print()

                                  i=input("Any other enquiry (yes/no): ").lower()
                                  if i=="no":
                                         print()
                                         break 
                       else:
                                 break             
                                     
           case 2:                   
                  str="""----- Welcome to Badrinath ----

1. Place Information
2. Hotel & Food Cost
3. Transport Cost
4. VIP Darshan
5. Total Budget Calculator
6. Things to Carry
7. Back"""  
                  while True :  
                       print()  
                       print(str)
                       i=int(input("enter your enquiery : "))
                       if i==1:
                           info="""
                            
******** BADRINATH ********

Location : Chamoli, Uttarakhand
Famous For : Lord Vishnu Temple
Height : 3,133 m
Best Time : May–June, September–October
Trip Duration : 1–2 Days
Temple Open : May to October/November"""
                           print()
                           print(info)
                           print()
                           i=input("Any other enquiry (yes/no)").lower()
                           if i=="no":
                                break
                       elif i==2:
                            print("****** HOTEL & FOOD ******")
                            print()
                            print("HOTEL")
                            print("Budget Hotel  = ₹1000/night")
                            print("Deluxe Hotel  = ₹2500/night")
                            print("Luxury Hotel  = ₹5000/night")
                            print()
                            print("FOOD")
                            print("Breakfast = ₹150/person")
                            print("Lunch     = ₹250/person")
                            print("Dinner    = ₹300/person")
                            print()

                            i=input("Any other enquiry (yes/no): ").lower()
                            if i=="no":
                                 break

                       elif i==3:
                           print("****** TRANSPORT ******")
                           print()
                           print("Bus = ₹2500")
                           print("Taxi = ₹4500")
                           print("Private Car = ₹7500")
                           print()

                           i=input("Any other enquiry (yes/no): ").lower()
                           if i=="no":
                                print()
                                break
 
                       elif i==4:
                          print("****** BADRINATH VIP DARSHAN ******")
                          print()
                          print("Special Darshan Ticket : ₹300/person")
                          print("Morning Darshan : 4:30 AM - 1:00 PM")
                          print("Evening Darshan : 4:00 PM - 9:00 PM")
                          print("Advance Booking Available")
                          print()

                          i=input("Any other enquiry (yes/no): ").lower()
                          if i=="no":
                                print()
                                break

                       elif i==5:
                          print("\n***** BADRINATH BUDGET CALCULATOR *****\n")

                          day=int(input("Stay duration (days): "))

                          print("\n1. Bus")
                          print("2. Taxi")
                          print("3. Private Car")
                          trnp=int(input("Select transport: "))

                          print("\n1. Budget Hotel")
                          print("2. Deluxe Hotel")
                          print("3. Luxury Hotel")
                          htl=int(input("Select hotel: "))

                          print("\n1. Simple Meal")
                          print("2. Standard Meal")
                          print("3. Premium Meal")
                          food=int(input("Select food: "))

                          print("\n1. Yes")
                          print("2. No")
                          vip=int(input("Need VIP Darshan? : "))

                          total=0

                       
                          match trnp:
                                case 1:
                                  print("\nBus : ₹2500")
                                  total+=2500
                                case 2:
                                   print("\nTaxi : ₹4500")
                                   total+=4500
                                case 3:
                                   print("\nPrivate Car : ₹7500")
                                   total+=7500
                                       
                          match htl:
                             case 1:
                                print("Budget Hotel :",1000*day)
                                total+=1000*day
                             case 2:
                                print("Deluxe Hotel :",2500*day)
                                total+=2500*day
                             case 3:
                                 print("Luxury Hotel :",5000*day)
                                 total+=5000*day

                          match food:
                             case 1:
                                 print("Simple Meal :",500*day)
                                 total+=500*day
                             case 2:
                                 print("Standard Meal :",700*day)
                                 total+=700*day
                             case 3:
                                  print("Premium Meal :",1000*day)
                                  total+=1000*day

 
                          if vip==1:
                                print("VIP Darshan : ₹300")
                                total+=300

                          print("\n----------------------------")
                          print("Total Expenses : ₹",total)

                          extra=total*0.20
                          print("Extra Expenses (20%) : ₹",extra)

                          print("Final Budget : ₹",total+extra)
                          print("----------------------------")

                          i=input("Any other enquiry (yes/no): ").lower()
                          if i=="no":
                                   print()
                                   break
                          elif i==6:

                              print("****** THINGS TO CARRY ******")
                              print()
                              print("1. Aadhaar Card / ID Proof")
                              print("2. Warm Clothes")
                              print("3. Comfortable Walking Shoes")
                              print("4. Raincoat / Umbrella")
                              print("5. Water Bottle")
                              print("6. Personal Medicines")
                              print("7. Mobile Charger / Power Bank")
                              print("8. Sunglasses & Sunscreen")
                              print("9. Cash (Limited ATMs)")
                              print("10. Small Backpack")
                              print()

                              i=input("Any other enquiry (yes/no): ").lower()
                              if i=="no":
                                     print()
                                     break
                          else:
                               print()
                               break

           case 3:
                  str="""----- Welcome to Gangotri ----

1. Place Information
2. Hotel & Food Cost
3. Transport Cost
4. Total Budget Calculator
5. Things to Carry
6. Back"""       
                  while True :  
                       print()  
                       print(str)
                       i=int(input("enter your enquiery : "))
                       if i==1:
                           info="""
                            ******** Gangotri ********


Location : Uttarkashi, Uttarakhand
Famous For : Origin of River Ganga
Height : 3,100 m
Best Time : May–June, September–October
Trip Duration : 1–2 Days
Temple Open : May to October/November"""
                           print()
                           print(info)
                       elif i==2:
                             print("****** HOTEL & FOOD ******")
                             print()
                             print("HOTEL")
                             print("Budget Hotel  = ₹800/night")
                             print("Deluxe Hotel  = ₹2000/night")
                             print("Luxury Hotel  = ₹4000/night")
                             print()
                             print("FOOD")
                             print("Breakfast = ₹120/person")
                             print("Lunch     = ₹220/person")
                             print("Dinner    = ₹250/person")
                             print()

                             i=input("Any other enquiry (yes/no): ").lower()
                             if i=="no":
                                    print()
                                    break
                       elif i==3:
                            print("****** TRANSPORT ******")
                            print()
                            print("Bus = ₹2200")
                            print("Taxi = ₹4000")
                            print("Private Car = ₹7000")
                            print()

                            i=input("Any other enquiry (yes/no): ").lower()
                            if i=="no":
                                  print()
                                  break

                       elif i==4:
                           print("****** GANGOTRI VIP DARSHAN ******")
                           print()
                           print("Special Darshan Pass : ₹500/person")
                           print()
                           print("Temple Timing : 6:15 AM - 2:00 PM")
                           print("Evening Darshan : 3:00 PM - 9:30 PM")
                           print("Priority Entry Available")
                           print()

                           i=input("Any other enquiry (yes/no): ").lower()
                           if i=="no":
                              print()
                              break

                       elif i==5:
                          print()
                          print("***** GANGOTRI BUDGET CALCULATOR *****")
                          print()

                          day=int(input("Stay duration (days): "))

                          print()
                          print("1. Bus")
                          print("2. Taxi")
                          print("3. Private Car")
                          trnp=int(input("Select mode of transport: "))

                          print()
                          print("1. Budget Hotel")
                          print("2. Deluxe Hotel")
                          print("3. Luxury Hotel")
                          htl=int(input("Select hotel category: "))

                          print()
                          print("1. Simple Meal")
                          print("2. Standard Meal")
                          print("3. Premium Meal")
                          food=int(input("Select food type: "))

                          print()
                          print("1. Yes")
                          print("2. No")
                          vip=int(input("Do you want VIP Darshan? : "))

                          print()
                          total=0


                          match trnp:
                             case 1:
                                 print("------Total Expenses------")
                                 print("Bus ₹",2200)
                                 total+=2200
                             case 2:
                                 print("------Total Expenses------")
                                 print("Taxi ₹",4000)
                                 total+=4000
                             case 3:
                                 print("------Total Expenses------")
                                 print("Private Car ₹",7000)
                                 total+=7000

   
                          match htl:
                              case 1:
                                 print("Budget Hotel ₹",800*day)
                                 total+=800*day
                              case 2:
                                 print("Deluxe Hotel ₹",2000*day)
                                 total+=2000*day
                              case 3:
                                 print("Luxury Hotel ₹",4000*day)
                                 total+=4000*day


                          match food:
                             case 1:
                                print("Simple Meal ₹",400*day)
                                total+=400*day
                             case 2:
                                print("Standard Meal ₹",600*day)
                                total+=600*day
                             case 3:
                                print("Premium Meal ₹",900*day)
                                total+=900*day

   
                          match vip:
                              case 1:
                                 print("VIP Darshan ₹500")
                                 total+=500
                              case 2:
                                 pass

                          print()
                          print("------------------------------")
                          print("Total Expenses : ₹",total)
                          print()

                          extra=total*0.20
                          print("Extra Expenses (20%) : ₹",extra)
                          print()
 
                          print("Final Budget : ₹",total+extra)
                          print("------------------------------")

                          i=input("Any other enquiry (yes/no): ").lower()
                          if i=="no":
                               print()
                               break
                       elif i==6:

                              print("****** THINGS TO CARRY ******")
                              print()
                              print("1. Aadhaar Card / ID Proof")
                              print("2. Trekking Shoes")
                              print("3. Warm Woollen Clothes")
                              print("4. Raincoat / Umbrella")
                              print("5. Walking Stick (Optional)")
                              print("6. Water Bottle")
                              print("7. Personal Medicines")
                              print("8. Power Bank")
                              print("9. Dry Fruits / Snacks")
                              print("10. Backpack")
                              print()

                              i=input("Any other enquiry (yes/no): ").lower()
                              if i=="no":
                                     print()
                                     break   
                       else:
                            break
           case 4:
                  str="""----- Welcome to Yamunotri ----

1. Place Information
2. Hotel & Food Cost
3. Transport Cost
4. Pony/palki/ropeway
5. Total Budget Calculator
6. Things to Carry
7. Back"""  
                  while True :  
                       print()  
                       print(str)
                       i=int(input("enter your enquiery : "))
                       if i==1:
                           info="""
                            ******** Yamunotri ********

Location : Uttarkashi, Uttarakhand
Famous For : Origin of River Yamuna
Height : 3,293 m
Best Time : May–June, September–October
Trip Duration : 1–2 Days
Temple Open : May to October/November""" 
                           print()
                           print(info)
                       elif i==2:
                              print("****** HOTEL & FOOD ******")
                              print()
                              print("HOTEL")
                              print("Budget Hotel = ₹800/night")
                              print("Deluxe Hotel = ₹1800/night")
                              print("Luxury Hotel = ₹3500/night")
                              print()
                              print("FOOD")
                              print("Breakfast = ₹120/person")
                              print("Lunch     = ₹220/person")
                              print("Dinner    = ₹250/person")
                              print()

                              i=input("Any other enquiry (yes/no): ").lower()
                              if i=="no":
                                     print()
                                     break

                       elif i==3:
                              print("****** TRANSPORT ******")
                              print()
                              print("Bus = ₹2200")
                              print("Taxi = ₹4000")
                              print("Private Car = ₹7000")
                              print()

                              i=input("Any other enquiry (yes/no): ").lower()
                              if i=="no":
                                     print()
                                     break

                       elif i==4:
                              print("****** PONY / PALKI / ROPEWAY ******")
                              print()
                              print("Pony     = ₹1800/person")
                              print("Palki    = ₹4500/person")
                              print("Ropeway  = ₹1000/person (One Way)")
                              print()

                              i=input("Any other enquiry (yes/no): ").lower()
                              if i=="no":
                                     print()
                                     break

                       elif i==5:
                              print()
                              print("***** YAMUNOTRI BUDGET CALCULATOR *****")
                              print()

                              day=int(input("Stay duration (days): "))

                              print()
                              print("1. Bus")
                              print("2. Taxi")
                              print("3. Private Car")
                              trnp=int(input("Select mode of transport: "))

                              print()
                              print("1. Budget Hotel")
                              print("2. Deluxe Hotel")
                              print("3. Luxury Hotel")
                              htl=int(input("Select hotel category: "))

                              print()
                              print("1. Simple Meal")
                              print("2. Standard Meal")
                              print("3. Premium Meal")
                              food=int(input("Select food type: "))

                              print()
                              print("1. Pony")
                              print("2. Palki")
                              print("3. Ropeway")
                              print("4. No Need")
                              service=int(input("Select service: "))

                              print()
                              total=0

                              match trnp:
                                     case 1:
                                            print("------Total Expenses------")
                                            print()
                                            print("Bus ₹",2200)
                                            total+=2200
                                     case 2:
                                            print("------Total Expenses------")
                                            print()
                                            print("Taxi ₹",4000)
                                            total+=4000
                                     case 3:
                                            print("------Total Expenses------")
                                            print()
                                            print("Private Car ₹",7000)
                                            total+=7000

                              match htl:
                                     case 1:
                                            print()
                                            print("Budget Hotel ₹",800*day)
                                            total+=800*day
                                     case 2:
                                            print()
                                            print("Deluxe Hotel ₹",1800*day)
                                            total+=1800*day
                                     case 3:
                                            print()
                                            print("Luxury Hotel ₹",3500*day)
                                            total+=3500*day

                              match food:
                                     case 1:
                                            print()
                                            print("Simple Meal ₹",400*day)
                                            total+=400*day
                                     case 2:
                                            print()
                                            print("Standard Meal ₹",600*day)
                                            total+=600*day
                                     case 3:
                                            print()
                                            print("Premium Meal ₹",900*day)
                                            total+=900*day

                              match service:
                                     case 1:
                                            print()
                                            print("Pony ₹1800")
                                            total+=1800
                                     case 2:
                                            print()
                                            print("Palki ₹4500")
                                            total+=4500
                                     case 3:
                                            print()
                                            print("Ropeway ₹1000")
                                            total+=1000
                                     case 4:
                                            print()
                                            print("Service ₹0")

                              print()
                              print("------------------------------")
                              print("Total Expenses : ₹",total)
                              print()

                              extra=total*0.20
                              print("Extra Expenses (20%) : ₹",extra)
                              print()

                              print("Final Budget : ₹",total+extra)
                              print("------------------------------")

                              i=input("Any other enquiry (yes/no): ").lower()
                              if i=="no":
                                     print()
                                     break
                       elif i==6:

                              print("****** THINGS TO CARRY ******")
                              print()
                              print("1. Aadhaar Card / ID Proof")
                              print("2. Trekking Shoes")
                              print("3. Warm Woollen Clothes")
                              print("4. Raincoat / Umbrella")
                              print("5. Walking Stick (Optional)")
                              print("6. Water Bottle")
                              print("7. Personal Medicines")
                              print("8. Power Bank")
                              print("9. Dry Fruits / Snacks")
                              print("10. Backpack")
                              print()

                              i=input("Any other enquiry (yes/no): ").lower()
                              if i=="no":
                                     print()
                                     break 
                       else:  
                              print()
                              break
               
           case 5:      
                        budget = int(input("Enter your budget :"))
                        print()
                        if budget <= 20000:
                                     print()
                                     print("****** ECONOMY PLAN ******")
                                     print()
                                     print("Transport : Bus")
                                     print("Stay      : Dharamshala / Budget Hotel")
                                     print("Food      : Simple Meal")
                                     print("Duration  : 2-3 Days")
                                     print("Darshan   : Normal Darshan")
                                     print("Suitable  : Solo / Low Budget Traveller")

                        elif budget <= 50000:
                                     print()
                                     print("****** STANDARD PLAN ******")
                                     print()
                                     print("Transport : Bus + Taxi")
                                     print("Stay      : Budget / Deluxe Hotel")
                                     print("Food      : Standard Meal")
                                     print("Duration  : 3-5 Days")
                                     print("Darshan   : Normal + Special Entry")
                                     print("Suitable  : Family / Friends Trip")

                        elif budget <= 100000:
                                     print()
                                     print("****** PREMIUM PLAN ******")
                                     print()
                                     print("Transport : Private Taxi / Car")
                                     print("Stay      : Deluxe Hotel")
                                     print("Food      : Premium Meal")
                                     print("Duration  : 5-7 Days")
                                     print("Darshan   : VIP Darshan")
                                     print("Suitable  : Comfortable Family Trip")

                        else:
                                     print()
                                     print("****** LUXURY PLAN ******")
                                     print()
                                     print("Transport : Private Luxury Vehicle")
                                     print("Stay      : Luxury Hotel")
                                     print("Food      : Premium Food")
                                     print("Duration  : 7+ Days")
                                     print("Darshan   : VIP Darshan")
                                     print("Suitable  : Luxury Pilgrimage Trip")

                        print()
                        print("*******************************")
                        print("Plan Recommended Successfully")
                        print("*******************************")

                        i=input("Any other enquiry (yes/no): ").lower()
                        if i=="no":
                               print()
                               break
           case 6:
                   break