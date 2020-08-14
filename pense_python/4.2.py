import turtle
import math

def linha(t, n, comp, ang):
    for i in range(n):
        t.fd(comp)
        t.lt(ang)

def arco(t, r, ang):
    arc_comp = 2 * math.pi * r * abs(ang) / 360
    n = int(arc_comp / 4) + 3
    step_comp = arc_comp / n
    step_ang = float(ang) / n
    t.lt(step_ang/2)
    linha(t, n, step_comp, step_ang)
    t.rt(step_ang/2)

def petala(t, r, ang):
    for i in range(2):
        arco(t, r, ang)
        t.lt(180-ang)

def flor(t, n, r, ang):
    for i in range(n):
        petala(t, r, ang)
        t.lt(360.0/n)

def mover(t, comp):
    t.pu()
    t.fd(comp)
    t.pd()

bob = turtle.Turtle()

mover(bob, -100)
flor(bob, 7, 60.0, 60.0)

mover(bob, 100)
flor(bob, 10, 40.0, 80.0)

mover(bob, 100)
flor(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()