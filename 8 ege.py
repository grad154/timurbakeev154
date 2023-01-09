#s = "школа"
#n = 0
#for a in s:
    #for b in s:
        #for c in s:
            #if (a+b+c).count("к") == 1:
                #n += 1
#print(n)


s = "абвгд"
n = 0

for a in s:
    for b in s:
        for c in s:
            n += 1
print("Ответ равен ", n * 2)
