import math
n=int(input("Enter Number :"))
temp=n
sum=0
rev=0
while n:
    mod=n%10
    rev=rev*10+mod
    sum=sum+mod
    n=n//10
diff=abs(temp-rev)
print("Diff is ",diff)
final=diff+sum
print("Final is ",final)
print("Reverse is ",rev)
print("Sum is ",sum)

if final<=1:
       print("Not Prime Number")
else:
   i=2
   while i<=math.sqrt(final):
        if final%i==0:
              print("Not a Prime Number")
              break
        i=i+1
   else:
       print("Number is prime")     
        
         