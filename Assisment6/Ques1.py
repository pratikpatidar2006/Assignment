sal,credit_s,n_el=map(int,input("Enter salary , credit score , number of existing loan ").split())

if sal>=30000:
    if credit_s>=750:
        print("Your loan is approved")
    else:
       if n_el>=2:
         print("your loan is rejected")
       else:
         print("loan should be conditionaly approved")
else:
    print("Your loan is rejected")   


