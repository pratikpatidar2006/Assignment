"""
Smart Farming Irrigation System

A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

Input:
Soil Moisture = 25
Temperature = 36
Crop = wheat

Output:
Irrigation = High Water Supply
"""

mois=int(input("Soil Moisture: "))
temp=int(input("Temperature: "))
crop=input("Crop Type: ")
rain=input("Expeceted Rain: ")

if mois<=30:
   if temp>=35:
       if crop=="wheat":
           print("High Water Supply")
       else:
           print("Moderate Supply")
   else: 
       print("Moderate Supply")
else: 
    if mois<=60:
        if rain=="yes":
            print("Delay Irigation")
        else:
            print("Light Irigation")
    else: 
        print("NO Irigation")
