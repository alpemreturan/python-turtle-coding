from tkinter import N
import turtle
import colorsys

try:
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.speed(0)
    n = 36
    h = 0
    for i in range(460):
        c = colorsys.hsv_to_rgb(h, 1, 0.9)
        h += 1 / n
        t.color(c)
        t.left(155)
        for j in range(7):
            t.forward(300)
            t.right(150)

    turtle.done()
except turtle.Terminator:
    print("Turtle window closed.")