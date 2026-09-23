"""


6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0


"""


n=int(input("Enter size:"))
arr=[]
for i in range(n):
     x=int(input("Enter value of list:"))
     arr.append(x)
prime=[]
primecount=0
for i in arr: 
     count=0
     for j in range(1,i):
         if i%j==0:
              count+=1
     if count==1:
          prime.append(i)
          primecount+=1
print("Prime IDs :",prime)         
print("Sum :",sum(prime))
print("Max :",max(prime))
print("Count",primecount)