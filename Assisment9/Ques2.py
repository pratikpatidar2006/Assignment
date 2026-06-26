n=int(input("Enter number"))
cam=0
while n:
    if cam<n%10:
         cam=n%10
    n=n//10
print("Maximum number is ",cam)
    
     