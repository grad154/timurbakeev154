#перевод из десятичной системы счисления в любую другую
num = int(input('enter the num(Np): '))
ns = int(input('enter number system: '))
res = 0
y = 0
while num > 0:
   res = res +(num % 10)*(ns**y)
   y += 1
   num = num // 10  
print('result is: ', res)
   

