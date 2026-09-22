"""

2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []

"""

n=int(input("enter length of array "))
list=[]
sum=0
for i in range(n):
      x=input("enter salary of employee : ")
      list.append(x)
      sum=sum+int(x)
avg=sum/n
print("Average salary is :",avg)

for i in list[:]:
       if int(i)>avg:
            print("Salary greater than avg :",i)
       elif int(i)<15000:
            list.remove(i)
print("Final list: ",list)