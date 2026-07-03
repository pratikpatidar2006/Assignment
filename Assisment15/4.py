"""
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407

"""
a=int(input("Enter number one :"))
b=int(input("Enter number second :"))

while a<=b:
      temp=a
      sum=0
      l=len(str(a))
      while temp:
            mod=temp%10
            sum=sum+mod**l
            temp=temp//10
      if sum==a:
           if a>=10:
                print(a,end=" ")
      a+=1
      
