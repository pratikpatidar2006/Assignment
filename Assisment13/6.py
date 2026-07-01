"""
6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29

"""
import math
n=int(input("Enter Number :"))

while True:
      i=2
      n=n+1
      while i<=math.sqrt(n):
            if n%i==0:
                break
            i+=1
      else:
          print("Next Prime Number is ",n)
          break
