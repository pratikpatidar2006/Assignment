"""
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india

"""

n=input("enter string:")
count=0
max=0
n1=n.split(" ")
for ch in n1:
       if n.count(ch):
            count+=1
       if count>max:
            max=count
            result=ch
          
print(result)