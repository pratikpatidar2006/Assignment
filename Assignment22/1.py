"""
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc

"""

n=input("enter string:")
i=0
visited=""
max=0
result=""
r1=""
while i<len(n):
       if n[i] not in visited:
               visited=visited+n[i]  
               result=result+n[i]       
       else:                         
            if len(result)>max:      
                   max=len(result)
                   r1=result
            result=""

       i+=1
print(r1)
              
                