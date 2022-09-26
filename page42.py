num = int(input('enter the num : '))
ns = int(input('enter number system: '))
last = 0
restest = ('')
while num > 0:
   last = num % ns
   restest += str(last)
   num = num // ns
res = list(restest)
print(str(restest.revers()))
