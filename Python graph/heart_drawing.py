import turtle as t
import math

t.bgcolor("black")
t.speed(100)  # Kecepatan maksimum
t.color("red")
t.pensize(2)

def heart(n, scale=1):
    x = 15 * math.sin(n)**3
    y = 12 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x * scale, y * scale

scale_factor = 1  # Faktor skala awal

for i in range(18):
    t.pendown()
    for j in range(0, 100):
        x, y = heart(j / 15, scale_factor)
        t.goto(x, y)
    t.penup()
    t.right(20)
    scale_factor += 0.5  # Meningkatkan skala setiap hati baru

t.hideturtle()
t.done()