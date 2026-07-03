"""
5.
Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145

"""
a=int(input("Enter Number first :"))
b=int(input("Enter number second :"))

while a<=b:
      temp=a
      sum=0
      while temp:    
           mod=temp%10
           temp=temp//10
           prod=1
           while mod>0:
             prod=prod*mod 
             mod-=1
           sum=sum+prod
      if sum==a:
          print(a,end=" ")
      a+=1
       
               
