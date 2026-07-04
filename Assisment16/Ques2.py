"""WAP print Square, Cube and Square Root of all numbers from 1 to N"""
import math
n=int(input("enter number: "))
for i in range(1,n+1):
   print("Sqrt: ",i*i)
   print("cbrt: ",i*i*i)
   print(math.sqrt(i))   