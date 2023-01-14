from turtle import *
left(90)
for i in range(7):
    forward(300) #
    right(120)
pu() #поднимаем перо


for x in range(1,9):
    for y in range(1,10):
        goto(x*30, y*30) # так как испльзовали мастшабирование домножаем на 10
        dot(5)  # ставим точку
done()


