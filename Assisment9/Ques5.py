num=int(input("Entert number"))
i=0
count=0
while i<=n//2:
      if(num%i==0):
          count+=1
      i+=1
print(count)
