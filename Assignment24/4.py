"""

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

"""

n=int(input("enter length of array "))
list=[]
for i in range(n):
    x=int(input("Enter number : "))
    list.append(x)
prime=[]
for i in list[:]:
      i=int(i)
      count=0
      for v in range(1,i):
          if i%v==0:
              count+=1
      if count==1:
              prime.append(i)
print("Prime count :",len(prime))
print("Non prime count :",n-len(prime))
print("Maximum prime :",max(prime))
print("Prime number :",prime)
print("Sorted prime list: ",sorted(prime))