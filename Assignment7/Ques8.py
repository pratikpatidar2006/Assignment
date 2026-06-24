temp=int(input("Enter Temperature in celcius :"))

if temp>35:
    print("Weather Condition : Hot")
elif temp>=21:
    print("Weather Condition : Warm")
elif temp>=0:
    print("Weather Condition : Cold")
else:
    print("Weather Condition : Freezing")