"""
# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data


---
"""

n=input("enter string:")
n1=n.split(" ")
visited=""
for ch in n1:
      if ch in visited:
           count=visited.count(ch)
           print(ch,"(",count,")",end=" ")
      else: 
           print(ch,end=" ")
          

      visited=visited+ch
           