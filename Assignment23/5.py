"""
# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca
"""

n=input("enter string:")

count=0
max=0
word=""
i=0
while i<len(n):
      temp=""
      j=i
      while j<len(n):
           if n[j] not in temp:
              temp =temp+n[j] 
           else:
             break
           j+=1
      if len(temp)>max:
             max=len(temp)
             longest=temp
      i+=1
print("### Output:")
print(longest)