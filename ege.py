import math
n = 1000
lst = [1]
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            break
    else:
        lst.append(i)

print(lst)
Str1 = '>' + 39 * '0' + n * '1' + 39 * '2'

for n in range(1, 1000):
  Str1 = '>' + 39 * '0' + n * '1' + 39 * '2'
  print(Str1)
  while ('>1' in Str1) or ('>2' in Str1) or ('>0' in Str1):
    if '>1' in Str1:
      Str1.replace('>1', '22>')
    if '>2' in Str1:
      Str1.replace('>2', '2>')
    if '>0' in Str1:
      Str1.replace('>0', '1>')
  spisok1 = list(Str1)
  print(spisok1)
  for g in lst:
    print(g)
    if g == sum(spisok1[:-1]):
      print(n)
      break
