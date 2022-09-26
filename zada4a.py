a =  int(input('enter the first num:'))
b = int(input('enter the second num:'))
count = 0
spis = []
for i in range(a,b+1):
   spis.append(i)
print('spis is ',spis)
for n in spis:
   print('n is:',n)
   while n > 0:
      if n % 2 == 1:
         count += 1
      n = n // 2
print('count is: ', count)
