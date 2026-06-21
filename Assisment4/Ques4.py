hrs,minutes=map(int,input("enter your time in hrs and minutes").split())
speed = float(input("Enter Speed in km/h"))
minutes=minutes/60
time=float(hrs+minutes)
dist = speed*time
print("Distance Travelled :",dist)
print("Time in hours :",time)