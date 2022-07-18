file1 = open("10digits.txt", "w")

import math
def digitconcat(x, y):
    if y != 0:
        a = math.floor(math.log10(y))
    else:
        a = -1

    return int(x*10**(1+a)+y)

def uniquecheck(n):
   return [int(x) for x in set(str(n))]
   
d2=[]
d3=[]
d4=[]
d5=[]
d6=[]
d7=[]
d8=[]
d9=[]
finallist=[]
uniquenum=[]

for i in range(5, 50):
   d2.append(i*2)

for i in d2:
   for j in range(0, 10):
      if digitconcat(i, j)%3==0:
         if digitconcat(i, j)<100:
            d3.append(digitconcat(i, j)*10)
         if digitconcat(i, j)>100:
            d3.append(digitconcat(i, j))
d3.sort()
for i in d3:
   for j in range(0, 5):
      if digitconcat(i, j*2)%4==0:
         if digitconcat(i, j*2)<10**3:
            d4.append(digitconcat(i, j*2)*10)
         if digitconcat(i, j*2)>10**3:
            d4.append(digitconcat(i, j*2))
d4.sort                   
for i in d4:
   for j in range(0, 2):
      if digitconcat(i, j*5)<10**4:
         d5.append(digitconcat(i, j)*10)
      if digitconcat(i, j)>10**4:
         d5.append(digitconcat(i, j*5))
d5.sort()
for i in d5:
   for j in range(0, 5):
      if digitconcat(i, j*2)%3==0:
         if digitconcat(i, j*2)<10**5:
            d6.append(digitconcat(i, j)*10)
         if digitconcat(i, j*2)>10**5:
            d6.append(digitconcat(i, j*2))
d6.sort()
for i in d6:
   for j in range(0, 10):
      if digitconcat(i, j)%7==0:
         if digitconcat(i, j)<10**6:
            d7.append(digitconcat(i, j)*10)
         if digitconcat(i, j)>10**6:
            d7.append(digitconcat(i, j))
d7.sort()
for i in d7:
   for j in range(0, 5):
      if digitconcat(i, j*2)%8==0:
         if digitconcat(i, j*2)<10**7:
            d8.append(digitconcat(i, j*2)*10)
         if digitconcat(i, j*2)>10**7:
            d8.append(digitconcat(i, j*2))
d8.sort()
for i in d8:
   for j in range(0, 10):
      if digitconcat(i, j)%9==0:
         if digitconcat(i, j)<10**8:
            d9.append(digitconcat(i, j)*10)
         if digitconcat(i, j)>10**8:
            d9.append(digitconcat(i, j))
d9.sort()
for i in d9:
   finallist.append(i*10)

for i in finallist:
   if len(uniquecheck(i))==len(str(i)):
      print(i)
