"""
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
"""
n=int(input("Enter number of house :"))
i=1
while i<=n:
      a=int(input("Enter bill :"))
      if a<=100:
          bill=bill+5*a
      elif a<=200:
          bill=100*5+(a-100)*7
      else:
          bill=100*5+(a-100)*7+(a-200)*10
      i+=1
      print(bill)
