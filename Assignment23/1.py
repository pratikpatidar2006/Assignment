"""
1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

text
abcabcbb


Output:

text
abc


"""

n=input("enter string:")
visited=""
result=""
i=0
while i<len(n):
      if n[i] not in visited:
          visited=visited+n[i] 
          
      else:
          j=0
          x=i
          while j<len(visited) and x<len(n):
              result=result+n[x]
              print(x)
              x+=1
              j+=1
          if result==visited:
                  print(result)
          visited=""
          result=""
      i+=1
          
              
          