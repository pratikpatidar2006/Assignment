"""

---

8.

=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}

"""

d=[]
n=int(input("Enter books"))

for i in range(n):
    d.append(input())

print(d)
book={}
for word in d:
    book[word]=book.get(word,0)+1
print(book)
    