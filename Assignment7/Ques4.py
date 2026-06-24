amount=int(input("Enter amount"))

if amount>=5000:
     discount=amount*(20/100)
     print("Final Amount:",amount-discount)

elif amount>=2000:
     discount=amount*(10/100)
     print("Final Amount:",amount-discount)

else:
     discount=amount*(5/100)
     print("Final Amount:",amount-discount)