"""

6.

=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

---

"""

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
d={}

for down in cities:
       d[down]=d.get(down,0)+1

print(d[down])
print(d)