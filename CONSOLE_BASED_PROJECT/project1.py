print()
print("\t\t  RESTAURANT BILL MAKING SYSTEM ")
print("\t\t --------------------------------")
print()
print()
print("\t\t\t\t MENU ")
print("\t\t\t\t........")
print()
print("\t\t     WELCOME IN PREET RESTAURANT ")
print("\t\t .....................................")
print()
sum=0
bill=""
while True :
    print("1. TEA & COFFEE")
    print("2. REFRESHMENTS")
    print("3. DESERT")
    print("4. APPETIZIERS")
    print("5. MAIN COURSE")
    print("6. Exit... THANKYOU")
    print()

    o=int(input(" please enter for check menu : "))
    if o==1:
        print()
        print(" HT.  HOT TEA                $40 \t   MT.  MILK TEA       $45")
        print(" KC.  KULHAD COFFEE          $40 \t   BT.  BLACK TEA      $45")
        print(" CC.  COLD COFFEE            $40 \t   LT.  LEMON TEA      $45")
        print(" CCC. CHOCOLATE COLD COFFEE  $139")
        print(" MCC. MOCHA COLD COFFEE      $250")
        sum=0
        while True :  
               print()
               a=input("Enter your choice :").upper()
               if a=="HT":
                     b=int(input(" Quantity :"))
                     c=b*40
                     bill=bill+"HOT TEA                  "+str(c)+"\t"+str(b)+"\n"
                     sum=sum+c
               if a=="KC":
                     b=int(input(" Quantity :"))
                     c=b*40
                     bill=bill+"KULHAD COFFEE            "+str(c)+"\t"+str(b)+"\n"
                     sum=sum+c
               if a=="CC":
                     b=int(input(" Quantity :"))
                     c=b*40
                     sum=sum+c
                     bill=bill+"COLD COFFEE              "+str(c)+"\t"+str(b)+"\n"
               if a=="CCC":
                     b=int(input(" Quantity :"))
                     c=b*139
                     sum=sum+c
                     bill=bill+"CHOCOLATE COLD COFFEE    "+str(c)+"\t"+str(b)+"\n"
               if a=="MCC":
                     b=int(input(" Quantity :"))
                     c=b*250 
                     sum=sum+c
                     bill=bill+"MOCHA COLD COFFEE        "+str(c)+"\t"+str(b)+"\n"
               if a=="MT":
                     b=int(input(" Quantity :"))
                     c=b*45
                     sum=sum+c
                     bill=bill+"MILK TEA                 "+str(c)+"\t"+str(b)+"\n"
               if a=="BT":
                     b=int(input(" Quantity :"))
                     c=b*40
                     sum=sum+c
                     bill=bill+"BLACK TEA                "+str(c)+"\t"+str(b)+"\n"
               if a=="LT":
                     b=int(input(" Quantity :"))
                     c=b*40
                     sum=sum+c
                     bill=bill+"LEMON TEA                "+str(c)+"\t"+str(b)+"\n"
               elif a=="ok": 
                     print()
                     break
                     

               
                    

                                       
    if o==2:
         
        print()
        print(" WB.  WATER BOTTLE            $25")
        print(" SD.  SOFT DRINK              $35")
        print(" MSD. MASALA SOFT DRINK       $35")  
        print(" LS.  LEMON SHIKANJI          $35")
        print(" MF.  MIX FRUIT JUICE         $35")
        print(" LM.  LIME SODA               $35")
        print(" SLD. SWEETLEMON DRINK        $45")
        print(" ED.  ENERGY DRINK            $45")
        print()
        while True :  
               print()
               a=input("Enter your choice :").upper()
               if a=="WB":
                     b=int(input(" Quantity :"))
                     c=b*25 
                     sum=sum+c
                     bill=bill+"WATER BOTTLE             "+str(c)+"\t"+str(b)+"\n"
             
               if a=="SD":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"SOFT DRINK               "+str(c)+"\t"+str(b)+"\n"
 
               if a=="MSD":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"MASALA SOFT DRINK        "+str(c)+"\t"+str(b)+"\n"
               if a=="LS":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"LEMON SHIKANJI           "+str(c)+"\t"+str(b)+"\n"
               if a=="MF":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"MIX FRUIT JUICE          "+str(c)+"\t"+str(b)+"\n"
               if a=="LM":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"LIME SODA                "+str(c)+"\t"+str(b)+"\n"
               if a=="SLD":
                     b=int(input(" Quantity :"))
                     c=b*45
                     sum=sum+c
                     bill=bill+"SWEETLEMON DRINK         "+str(c)+"\t"+str(b)+"\n"
               if a=="ED":
                     b=int(input(" Quantity :"))
                     c=b*45
                     sum=sum+c
                     bill=bill+"ENERGY DRINK             "+str(c)+"\t"+str(b)+"\n"
               elif a=="ok":
                     print()
                     break
                     



    if o==3:
       print() 
       print("GJ.  GULABJAMUN              $29")
       print("VI.  VANILLA ICECREAM        $29")
       print("CI.  CHOCLATE ICECREAM       $29")
       print("BR.  BROWINE                 $29")
       print("SB.  SIZZLIER BROWNIE        $29")
       print("BI.  BROWNIE ICECREAM        $29")
       print()
       while True:
               print()
               a=input("Enter your choice :").upper()
               if a=="GJ":
                     b=int(input(" Quantity :"))
                     c=b*29 
                     sum=sum+c
                     bill=bill+"GULABJAMUN              "+str(c)+"\t"+str(b)+"\n"
               if a=="CI":
                     b=int(input(" Quantity :"))
                     c=b*29 
                     sum=sum+c
                     bill=bill+"CHOCOLATE ICECREAM      "+str(c)+"\t"+str(b)+"\n"

               if a=="VI":
                     b=int(input(" Quantity :"))
                     c=b*29
                     sum=sum+c
                     bill=bill+"VANILLA ICECREAM        "+str(c)+"\t"+str(b)+"\n"

               if a=="BR":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"BROWINE                 "+str(b)+"\t"+str(b)+"\n"
               if a=="SB":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"SIZZLIER BROWNIE        "+str(c)+"\t"+str(b)+"\n"
               if a=="MF":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"MIX FRUIT JUICE         "+str(c)+"\t"+str(b)+"\n"
               elif a=="ok":
                     print()
                     break


    if o==4:
       
       print()
       print(" $49        AV.  ALOO VADA")
       print(" $39        IP.  INDORI POHA")
       print(" $110       KP.  KAJU POHA") 
       print(" $45        KHP. KHOPRA PATIES")
       print(" $50        BPB. BUTTER PAV BHAAJI")
       print(" $55        CPB. CHEESE PAV BHAAJI")
       print(" $60        VB.  VEG BURGER")
       print(" $70        CB.  CHEASE BURGER")
       print(" $70        GVS. GRILL VEG SANDWICH")
       print(" $75        GPS. GRILL PANNER SANDWITCH")
       print(" $70        GCS. GRILL CHEASE SANDWICH ")
       print(" $70        FF.  FRENCH FRIES")
       print(" $70        CP.  CHEESE POPS")
       print()
       while True: 
               print()
               a=input("Enter your choice :").upper()
               if a=="AV":
                     b=int(input(" Quantity :"))
                     c=b*49
                     sum=sum+c
                     bill=bill+"AALO VADA               "+str(c)+"\t"+str(b)+"\n"
               if a=="IP":
                     b=int(input(" Quantity :"))
                     c=b*39
                     sum=sum+c
                     bill=bill+"INDORI POHA             "+str(c)+"\t"+str(b)+"\n"

               if a=="KP":
                     b=int(input(" Quantity :"))
                     c=b*110
                     sum=sum+c
                     bill=bill+"KAJU POHA               "+str(c)+"\t"+str(b)+"\n"

               if a=="KHP":
                     b=int(input(" Quantity :"))
                     c=b*45
                     sum=sum+c
                     bill=bill+"KHOPRA PATIES            "+str(c)+"\t"+str(b)+"\n"
               if a=="BPB":
                     b=int(input(" Quantity :"))
                     c=b*50
                     sum=sum+c
                     bill=bill+"BUTTER PAAV BHAAJI       "+str(c)+"\t"+str(b)+"\n"
               if a=="CPB":
                     b=int(input(" Quantity :"))
                     c=b*55 
                     sum=sum+c
                     bill=bill+"CHEESE PAV BHAAJI        "+str(c)+"\t"+str(b)+"\n"
               if a=="VB":
                     b=int(input(" Quantity :"))
                     c=b*60
                     sum=sum+c
                     bill=bill+"VEG BURGER               "+str(c)+"\t"+str(b)+"\n"

               if a=="CB":
                     b=int(input(" Quantity :"))
                     c=b*70
                     sum=sum+c
                     bill=bill+"CHEASE BURGER            "+str(c)+"\t"+str(b)+"\n"
               if a=="GVS":
                     b=int(input(" Quantity :"))
                     c=b*70
                     sum=sum+c
                     bill=bill+"GRILL VEG SANDWITCH      "+str(c)+"\t"+str(b)+"\n"

               if a=="GPS":
                     b=int(input(" Quantity :"))
                     c=b*75
                     sum=sum+c
                     bill=bill+"GRILL PANEER SANDWITCH   "+str(c)+"\t"+str(b)+"\n"

               if a=="GCS":
                     b=int(input(" Quantity :"))
                     c=b*70 
                     sum=sum+c
                     bill=bill+"GRILL CHEASE SANDWITCH   "+str(c)+"\t"+str(b)+"\n"
               if a=="FF":
                     b=int(input(" Quantity :"))
                     c=b*70 
                     sum=sum+c
                     bill=bill+"FRENCH FRIES             "+str(c)+"\t"+str(b)+"\n"
               if a=="CP":
                     b=int(input(" Quantity :"))
                     c=b*70
                     sum=sum+c
                     bill=bill+"CHEESE POPS              "+str(c)+"\t"+str(b)+"\n"
               elif a=="ok":
                     print()
                     break

    if o==5:
       
       print()
       print(" TBT.  TAWA BUTTER ROTI        $15  ")
       print(" TR.   TAWA ROTI               $12  ")
       print(" TABR. TANDORI BUTTER ROTI     $22 ") 
       print(" TR.   TAWA  ROTI              $15  ")
       print(" TAR.  TANDOORI ROTI           $18  ")
       print(" PN.   PLAN NAAN               $25  ")
       print(" MR.   MISSI ROTI              $30  ")
       print(" BN.   BUTTER NAAN             $35  ")
       print(" PP.   PLAIN PARATHA           $25  ")
       print(" LP.   LACHHA PARATHA          $35  ")
       print(" AP.   AALO PARATHA            $35  ")
       print(" PP.   PANEER PARATHA          $59  ")
       print(" SP.   SATTU PARATHA           $59  ")
       print(" BB.   BREAD BASKET            $179")
       print(" DM.   DAL MAKHNI              $80")
       print(" DF.   DAL FRY                 $120")
       print(" ST.   SEV TAMATOR             $140")
       print(" PC.   PANEER CLASSIC          $180")
       print(" PBM.  PANEER BUTTER MASALA    $280")
       print(" PM.   PANEER MUSHROOM         $280")
       print(" PAK.   PANEER KADAI            $280")
       print(" PTM.  PANEER TIKKA MASALA     $380")
       print(" SP.   SHAHI PANEER            $280")
       print(" MP.   MUTTER PANEER           $260")
       print(" KC.   KAJU CURRY              $360")
       print(" PK.   PANNER KAJU             $320")
       print()
       while True:
               print()
               a=input("Enter your choice :").upper()
               if a=="TBR":
                     b=int(input(" Quantity :"))
                     c=b*15
                     sum=sum+c
                     bill=bill+"TAWA BUTTER ROTI       "+str(c)+"\t"+str(b)+"\n"

               if a=="TR":
                     b=int(input(" Quantity :"))
                     c=b*12
                     sum=sum+c
                     bill=bill+"TAWA ROTI              "+str(c)+"\t"+str(b)+"\n"
               if a=="TABR":
                     b=int(input(" Quantity :"))
                     c=b*22
                     sum=sum+c
                     biLl=bill+"TANDORI BUTTER ROTI    "+str(c)+"\t"+str(b)+"\n"

               if a=="TAR":
                     b=int(input(" Quantity :"))
                     c=b*15
                     sum=sum+c
                     bill=bill+"TANDOORI ROTI          "+str(c)+"\t"+str(b)+"\n"

               if a=="PN":
                     b=int(input(" Quantity :"))
                     c=b*25
                     sum=sum+c
                     bill=bill+"PLAN NAAN              "+str(c)+"\t"+str(b)+"\n"
               if a=="LP":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"LACHHA PARATHA         "+str(c)+"\t"+str(b)+"\n"
               if a=="AP":
                     b=int(input(" Quantity :"))
                     c=b*35
                     sum=sum+c
                     bill=bill+"AALO PARATHA           "+str(c)+"\t"+str(b)+"\n"

               if a=="PP":
                     b=int(input(" Quantity :"))
                     c=b*59
                     sum=sum+c
                     bill=bill+"PANEER PARATHA         "+str(c)+"\t"+str(b)+"\n"

               if a=="SP":
                     b=int(input(" Quantity :"))
                     c=b*179
                     sum=sum+c
                     bill=bill+"SATTU PARATHA          "+str(c)+"\t"+str(b)+"\n"
               if a=="BB":
                     b=int(input(" Quantity :"))
                     c=b*80
                     sum=sum+c
                     biLl=bill+"BREAD BASKET           "+str(c)+"\t"+str(b)+"\n"

               if a=="DM":
                     b=int(input(" Quantity :"))
                     c=b*80
                     sum=sum+c
                     bill=bill+"DAL MAKHNI             "+str(c)+"\t"+str(b)+"\n"

               if a=="DF":
                     b=int(input(" Quantity :"))
                     c=b*120
                     sum=sum+c
                     bill=bill+"DAL FRY                "+str(c)+"\t"+str(b)+"\n"
               if a=="ST":
                     b=int(input(" Quantity :"))
                     c=b*140 
                     sum=sum+c
                     bill=bill+"SEV TAMATOR            "+str(c)+"\t"+str(b)+"\n"
               if a=="PC":
                     b=int(input(" Quantity :"))
                     c=b*180
                     sum=sum+c
                     bill=bill+"PANEER CLASSIC         "+str(c)+"\t"+str(b)+"\n"

               if a=="PBM":
                     b=int(input(" Quantity :"))
                     c=b*280
                     sum=sum+c
                     bill=bill+"PANNER BUTTER MASALA   "+str(c)+"\t"+str(b)+"\n"
               if a=="PAK":
                     b=int(input(" Quantity :"))
                     c=b*280
                     sum=sum+c
                     biLl=bill+"PANEER KADAI           "+str(c)+"\t"+str(b)+"\n"

               if a=="PTM":
                     b=int(input(" Quantity :"))
                     c=b*380
                     sum=sum+c
                     bill=bill+"PANEER TIKKA MASALA    "+str(c)+"\t"+str(b)+"\n"

               if a=="SP":
                     b=int(input(" Quantity :"))
                     c=b*280
                     sum=sum+c
                     bill=bill+"SHAHI PANEER           "+str(c)+"\t"+str(b)+"\n"
               if a=="MP":
                     b=int(input(" Quantity :"))
                     c=b*260
                     sum=sum+c
                     bill=bill+"MUTTER PANEER          "+str(c)+"\t"+str(b)+"\n"
               if a=="PC":
                     b=int(input(" Quantity :"))
                     c=b*360 
                     sum=sum+c
                     bill=bill+"KAJU CURRY             "+str(c)+"\t"+str(b)+"\n"
               if a=="PK":
                     b=int(input(" Quantity :"))
                     c=b*320
                     sum=sum+c
                     bill=bill+"PANEER KAAJU           "+str(c)+"\t"+str(b)+"\n"
               elif a=="ok":
                     print()
                     break

    if o==6:
       break   
print()
print("......... Preet The Dhabha ..........." )
print()
print(" Item                   Price  Qnt ")
print()
print(bill)
print("-----------------------------------")
print("                        CGST :",int(sum*3/100))
print("                 Total price :",sum)
print("                    Discount :",int(sum*10/100))
print("                 Final Bill  :",int(sum+(sum*3/100)-(sum*10/100)))
print()
print("    thankyou .. visit again ")