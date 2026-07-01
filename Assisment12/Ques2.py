import math
print
n=int(input("Enter Number:"))
temp=n
while True:
           i=2
           n+=1 
           while i<=math.sqrt(n):
                  if n%i==0: 
                    break
                  i+=1
           else:
                print("Next Prime Number is ",n) 
                break