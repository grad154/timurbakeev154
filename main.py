import turtle

def sqr(a):
  for i in range(4):
    tym.color(color[i%4])
    tym.forward(a)
    tym.left(90)

color = ['red', 'brown', 'green', 'blue']

tym = turtle.Turtle()
tym.speed(12)

dlina = 40
for i in range(60):
  tym.circle(dlina)
  tym.right(10)
  dlina = dlina + 4

#circle встроенная команда круга